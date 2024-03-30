import io
import pandas as pd
import yfinance as yf
from pandas_datareader import data as pdr
import datetime
import os
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    yf.pdr_override()
    start = "2023-01-01"
    end = "2024-01-01"
    
    stocks = ['MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO', 'DIS', 'XOM', 'GE',
          'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'MCD', 'MRK', 'MSFT', 'NKE', 'PFE',
          'PG', 'TRV', 'DOW', 'UNH', 'V', 'VZ', 'WMT', 'GOOGL', 'AMZN', 'CRM']

    # storing data if API does not work
    if not os.path.exists('data'):
        print('Creating data directory')
        os.makedirs('data')
        for ticker in stocks:
            file_name = 'data/' + ticker + '_' + start + '_to_' + end + '.csv'
            data = pdr.get_data_yahoo(ticker, start=start, end=end)
            data['Name'] = ticker
            data.to_csv(file_name)

    df_arr = []
    for (i, ticker) in enumerate(stocks):
        file_name = 'data/' + ticker + '_' + start + '_to_' + end + '.csv'
        data = pd.read_csv(file_name, parse_dates=['Date'], index_col=['Date'])
        df_arr.append(data)
    
    df = pd.concat(df_arr)
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'