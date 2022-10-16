# All companies >=$50b market cap (15-Aug-2021) https://www.nasdaq.com/market-activity/stocks/screener
TICKERS = {'AAPL', 'MSFT', 'AMZN', 'GOOG', 'FB', 'PTR', 'TSLA', 'BABA', 'TSM', 'BRK-B', 'V', 'JPM',
           'JNJ', 'WMT', 'NVDA', 'MA', 'UNH', 'HD', 'BAC', 'DIS', 'PG', 'PYPL', 'ASML', 'CMCSA', 'XOM',
           'ADBE', 'KO', 'VZ', 'INTC', 'TM', 'ORCL', 'CSCO', 'NFLX', 'PFE', 'NKE', 'T', 'ABT', 'CRM',
           'PEP', 'ABBV', 'CVX', 'MRK', 'LLY', 'WFC', 'ACN', 'AVGO', 'UPS', 'TMO', 'DHR', 'TXN', 'MCD',
           'MDT', 'COST', 'SAP', 'PDD', 'C', 'UL', 'LIN', 'HON', 'SHOP', 'PM', 'AZN', 'QCOM', 'BMY', 'UNP',
           'RY', 'NEE', 'NVO', 'BA', 'MS', 'AMGN', 'HDB', 'LOW', 'SNY', 'BLK', 'TD', 'SBUX', 'CHTR', 'RTX',
           'CAT', 'SCHW', 'HSBC', 'IBM', 'AXP', 'AMAT', 'BUD', 'SONY', 'INTU', 'GE', 'MMM', 'AMT', 'CVS',
           'TGT', 'DEO', 'DE', 'EL', 'BX', 'LMT', 'NVS', 'TMUS', 'BHP', 'BBL', 'SE', 'RDS-A', 'RIO', 'MRNA', 'GS',
           'AMD', 'SONY', 'SQ', 'ISRG', 'TTE', 'SNAP', 'NOW', 'JD', 'SPGI', 'GSK', 'ZM', 'VALE', 'INFY', 'SYK',
           'PLD', 'PLD', 'ZTS', 'BAM', 'MELI', 'BNTX', 'ABNB', 'ADP', 'BKNG', 'MO', 'ANTM', 'GILD', 'MDLZ', 'SNOW', 'USB', 'BTI',
           'TJX', 'BP', 'TEAM', 'CCI', 'FIS', 'LRCX', 'DUK', 'PNC', 'SHW', 'CB', 'MU', 'UBER', 'ENB', 'COF', 'BNS', 'GM', 'HCA', 'MMC',
           'TFC', 'DELL', 'CSX', 'CNI', 'ILMN', 'ABB', 'COP', 'CME', 'FDX', 'PBR', 'FISV', 'ITW', 'ADSK', 'EQIX', 'CI', 'MUFG', 'MCO',
           'BDX', 'EW', 'WBK', 'SO', 'EQNR', 'STLA', 'NIO', 'IBN', 'CL', 'SAN', 'REGN', 'ETN', 'BMO', 'NSC', 'VMW', 'ICE', 'ATVI', 'TWLO',
           'DASH', 'WM', 'ECL', 'BSX', 'D', 'ADI', 'AON', 'CVNA', 'EMR', 'APD', 'NTES', 'UBS', 'CPNG', 'RELX', 'WDAY', 'NOC', 'BSBR', 'DOCU',
           'ITUB', 'IDXX', 'NXPI', 'AMX', 'AMOV', 'TRI', 'PGR', 'HMC', 'RACE', 'SNP', 'FCX', 'DG', 'GD', 'PUK', 'LULU', 'PSA', 'CRWD', 'ALGN',
           'COIN', 'F', 'ING', 'MET', 'CM', 'CMG', 'BIDU', 'HUM', 'TAK', 'SCCO', 'MSCI', 'MNST', 'JCI', 'TWTR', 'BIIB', 'ROP', 'FTNT', 'EBAY',
           'VRTX', 'GPN', 'KLAC', 'TEL'}


# Macro economic indicators (mostly US) from the FRED database
# Detailed info on each indicator check on web: https://fred.stlouisfed.org/series/<indicator_name>
# DOC with the metrics and external exploratory Colab: https://docs.google.com/document/d/1Cf4C3Xz4_yitlzPaLEknHoDlw7KMXey4c49kZ7ucQEE/edit?usp=sharing

FRED_INDICATORS = ['GDP', 'GDPC1', 'GDPPOT', 'NYGDPMKTPCDWLD',         # 1. Growth
                   'CPIAUCSL', 'CPILFESL', 'GDPDEF',                   # 2. Prices and Inflation
                   'M1SL', 'WM1NS', 'WM2NS', 'M1V', 'M2V', 'WALCL',    # 3. Money Supply
                   'DFF', 'DTB3', 'DGS5', 'DGS10', 'DGS30', 'T5YIE',   # 4. Interest Rates
                   'T10YIE', 'T5YIFR', 'TEDRATE', 'DPRIME',            # 4. Interest Rates
                   'UNRATE', 'NROU', 'CIVPART', 'EMRATIO',             # 5. Employment
                   'UNEMPLOY', 'PAYEMS', 'MANEMP', 'ICSA', 'IC4WSA',   # 5. Employment
                   'CDSP', 'MDSP', 'FODSP', 'DSPIC96', 'PCE', 'PCEDG',  # 6. Income and Expenditure
                   'PSAVERT', 'DSPI', 'RSXFS',                         # 6. Income and Expenditure
                   'INDPRO', 'TCU', 'HOUST', 'GPDI', 'CP', 'STLFSI2',  # 7. Other indicators
                   'DCOILWTICO', 'DTWEXAFEGS', 'DTWEXBGS',             # 7. Other indicators
                   'GFDEBTN', 'GFDEGDQ188S',                           # 8. Gov-t debt
                   # 9. Additional indicators from IVAN
                   'DEXUSEU', 'GVZCLS', 'VIXCLS', 'DIVIDEND',
                   # 9. Additional indicators from IVAN
                   'MORTGAGE30US', 'SPCS20RSA'
                   ]

# Macro Indicators from QUANDL
QUANDL_INDICATORS = {'BCHAIN/MKPRU', 'USTREASURY/YIELD', 'USTREASURY/REALYIELD',  # 9. Additional indicators from IVAN
                     # 9. Additional indicators from IVAN
                     'MULTPL/SHILLER_PE_RATIO_MONTH', 'LBMA/GOLD'
                     }

# update period for each ind (Y=Yearly, Q=Quarterly, M=Monthly, W=Weekly, D=Daily)
INDICATORS_PERIODS = { # 1. Growth
                      'GDP': 'Q', 'GDPC1': 'Q', 'GDPPOT': 'Q', 'NYGDPMKTPCDWLD': 'Y',                
                      # 2. Prices and Inflation
                      'CPIAUCSL': 'M', 'CPILFESL': 'M', 'GDPDEF': 'Q',
                      # 3. Money Supply
                      'M1SL': 'M', 'WM1NS': 'W', 'WM2NS': 'W', 'M1V': 'Q', 'M2V': 'Q', 'WALCL': 'W',
                      # 4. Interest Rates
                      'DFF': 'D', 'DTB3': 'D', 'DGS5': 'D', 'DGS10': 'D', 'DGS30': 'D', 'T5YIE': 'D',
                      # 4. Interest Rates
                      'T10YIE': 'D', 'T5YIFR': 'D', 'TEDRATE': 'D', 'DPRIME': 'D',
                      # 5. Employment
                      'UNRATE': 'M', 'NROU': 'Q', 'CIVPART': 'M', 'EMRATIO': 'M',
                      # 5. Employment
                      'UNEMPLOY': 'M', 'PAYEMS': 'M', 'MANEMP': 'M', 'ICSA': 'W', 'IC4WSA': 'W',
                      # 6. Income and Expenditure
                      'CDSP': 'Q', 'MDSP': 'Q', 'FODSP': 'Q', 'DSPIC96': 'M', 'PCE': 'M', 'PCEDG': 'M',
                      # 6. Income and Expenditure
                      'PSAVERT': 'M', 'DSPI': 'M', 'RSXFS': 'M',
                      # 7. Other indicators
                      'INDPRO': 'M', 'TCU': 'M', 'HOUST': 'M', 'GPDI': 'Q', 'CP': 'Q', 'STLFSI2': 'W',
                      # 7. Other indicators
                      'DCOILWTICO': 'D', 'DTWEXAFEGS': 'D', 'DTWEXBGS': 'D',
                      # 8. Gov-t debt
                      'GFDEBTN': 'Q', 'GFDEGDQ188S': 'Q',
                      # 9. FRED: Additional indicators from IVAN
                      'DEXUSEU': 'D', 'GVZCLS': 'D', 'VIXCLS': 'D', 'DIVIDEND': 'Q',
                      # 9. FRED: Additional indicators from IVAN
                      'MORTGAGE30US': 'W', 'SPCS20RSA': 'M',
                      # 9.QUANDL: Additional indicators from IVAN
                      'BCHAIN_MKPRU': 'D', 'USTREASURY_YIELD': 'D', 'USTREASURY_REALYIELD': 'D',
                      'MULTPL_SHILLER_PE_RATIO_MONTH': 'M', 'LBMA_GOLD': 'D'
                      }
