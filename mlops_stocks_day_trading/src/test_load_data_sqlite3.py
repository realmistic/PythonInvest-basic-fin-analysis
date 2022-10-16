import pandas as pd

import os

# databases
import sqlite3

import datetime
import yfinance as yf

# data_sources CONSTANTS : TICKERS, etc.
import data_sources

# retry func() call for n times (default is 5)
def retry(func, times=5):
    for _ in range(times):
        try:
            return func()
        except Exception as e:
            print(e)
            continue


# Data storage class
class DataRepositorySqlLite:
    tickers_df: pd.DataFrame = None  # main in-memory storage of tickers stats
    ALL_TICKERS: data_sources.TICKERS

    # CLASS CONSTRUCTOR
    def __init__(self, db_path="data/tickers.db"):
        self.ticker_df = None
        self.TICKERS = data_sources.TICKERS

        # SQLLITE3
        self.db_conn_sqlite = None
        self.db_cur_sqlite = None
        # list of existing db files
        self.existing_db_files = [f for f in os.listdir("data/") if f.endswith(".db")]
        print(self.existing_db_files)
        # Create a db file if not there  : https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial
        self.db_conn_sqlite = sqlite3.connect(db_path)
        self.db_cur_sqlite = self.db_conn_sqlite.cursor()

        # if there is a table ==> let's load its contents to df_tickers, otherwise let's create it
        if self._db_check_table_exists("tickers"):
            self._db_read_all_records_from_db()
        else:  # not self._db_check_table_exists('tickers') ==TRUE
            self._db_create_table_tickers()

    # CLASS DESTRUCTOR
    def __del__(self):
        # close cursor
        self.db_conn_sqlite.close()

    # PROTECTED: CHECK IF A TABLE EXISTS
    def _db_check_table_exists(self, table_name: str = "tickers"):
        sql = f""" SELECT count(name) 
                    FROM sqlite_master 
                    WHERE type='table' 
                          AND name='{table_name}' """

        self.db_cur_sqlite.execute(sql)
        if self.db_cur_sqlite.fetchone()[0] == 1:
            return True
        else:
            return False

    # PROTECTED: CREATE A TABLE IF NOT EXISTS (SQLLITE3)
    def _db_create_table_tickers(self):
        # https://stackoverflow.com/questions/734689/sqlite-primary-key-on-multiple-columns
        sql = """CREATE TABLE "tickers" (
                "Date" TIMESTAMP,
                "Ticker" TEXT,
                "Open" REAL,
                "High" REAL,
                "Low" REAL,
                "Close" REAL,
                "Adj Close" REAL,
                "Volume" INTEGER,
                PRIMARY KEY (Date, Ticker)
                )"""
        self.db_cur_sqlite.execute(sql)
        self.db_conn_sqlite.commit()

    def _db_read_all_records_from_db(self):
        try:
            self.tickers_df = pd.read_sql("select * from tickers", self.db_conn_sqlite)
            self.tickers_df["Date"] = pd.to_datetime(
                self.tickers_df["Date"]
            )  # need correct type 'datetime' and not object
        except Exception as e:
            print(f"FAILED TO READ ALL RECORDS FROM DB: {e}")

    # PROTECTED: fetch stats from the API for 1 ticker and store to the DB
    def _fetch_ticker_incremental(self, ticker: str, period_days=1):
        max_data_date = None  # by default let's assume there is no data in DB
        incremental_df: pd.DataFrame = None

        if self.tickers_df is not None:
            max_data_date = self.tickers_df.Date.max()

        if max_data_date is None:
            max_data_date = datetime.datetime.strptime("2021-01-01", "%Y-%m-%d")

        start_date = max_data_date + datetime.timedelta(days=1)
        end_date = max_data_date + datetime.timedelta(days=1 + period_days)

        # try 5 times to get the incr. data for 1 ticker
        incremental_df = retry(
            lambda: yf.download(ticker, start=start_date, end=end_date)
        )
        incremental_df["Ticker"] = ticker  # define a new field

        print(
            f"downloaded records {incremental_df.shape} with min_date {incremental_df.index.min()} and max_date {incremental_df.index.max()}"
        )

        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
        try:
            incremental_df.to_sql(
                name="tickers",
                index=True,
                # index_label='',
                if_exists="append",
                con=self.db_conn_sqlite,
            )
            self.db_conn_sqlite.commit()

            incremental_df["Date"] = incremental_df.index
            # append_local_df with the new data
            # self._db_read_all_records_from_db()
            self.tickers_df = self.tickers_df.append(incremental_df, ignore_index=True)

        except Exception as e:
            print(f"SAVE TO DB IS NOT SUCCESSFUL: {e}")

    def fetch_ticker_incremental(self, ticker: str, period_days=1):
        self._fetch_ticker_incremental(ticker, period_days)
        print(f"Successfully fetched {ticker} for more {period_days}")

