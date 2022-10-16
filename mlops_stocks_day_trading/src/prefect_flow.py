from prefect import flow, task
from prefect.task_runners import SequentialTaskRunner


from load_data import DataRepository

@task (retries=3)
def get_new_tickers_data():
    repo = DataRepository()
    repo.fetch_ticker_incremental(ticker='GOOG', period_days=7)

@flow(name = "Data Flow", 
      task_runner = SequentialTaskRunner())
def full_cycle():
    """Call all data APIs to store the stats to DB"""
    get_new_tickers_data()
    return

if __name__ == "__main__":
    full_cycle()
