import datetime
import random
from random import randrange
import numpy as np
import pandas as pd


def _random_date(start,date_count):
    """This function generates a random date based on params
    Args:
        start (date object): the base date
        date_count (int): number of dates to be generated
    Returns:
        list of random dates

    """
    current = start
    while date_count > 0:
        curr = current + datetime.timedelta(days=randrange(42))
        yield curr
        date_count-=1
        
        

def generate_sample_data(row_count=100):
    """This function generates a random transaction dataset
    Args:
        row_count (int): number of rows for the dataframe
    Returns:
        a pandas dataframe

    """

    # sentinels
    startDate = datetime.datetime(2016, 1, 1, 13)
    serial_number_sentinel = 1000
    user_id_sentinel = 5001
    product_id_sentinel = 101
    price_sentinel = 2000

    # base list of attributes
    data_dict = {
        'Serial No':
        np.arange(row_count) + serial_number_sentinel,
        'Date':
        np.random.permutation(
            pd.to_datetime([
                x.strftime("%d-%m-%Y")
                for x in _random_date(startDate, row_count)
            ]).date),
        'User ID':
        np.random.permutation(
            np.random.randint(0, row_count, size=int(row_count / 10)) +
            user_id_sentinel).tolist() * 10,
        'Product ID':
        np.random.permutation(
            np.random.randint(0, row_count, size=int(row_count / 10)) +
            product_id_sentinel).tolist() * 10,
        'Quantity Purchased':
        np.random.permutation(np.random.randint(1, 42, size=row_count)),
        'Price':
        np.round(
            np.abs(np.random.randn(row_count) + 1) * price_sentinel,
            decimals=2),
        'User Type':
        np.random.permutation(
            [chr(random.randrange(97, 97 + 3 + 1)) for i in range(row_count)])
    }

    # introduce missing values
    for index in range(int(np.sqrt(row_count))):
        data_dict['Price'][np.argmax(
            data_dict['Price'] == random.choice(data_dict['Price']))] = np.nan
        data_dict['User Type'][np.argmax(
            data_dict['User Type'] == random.choice(
                data_dict['User Type']))] = np.nan
        data_dict['Date'][np.argmax(
            data_dict['Date'] == random.choice(data_dict['Date']))] = np.nan
        data_dict['Product ID'][np.argmax(data_dict['Product ID'] == random.
                                          choice(data_dict['Product ID']))] = 0
        data_dict['Serial No'][np.argmax(data_dict['Serial No'] == random.
                                         choice(data_dict['Serial No']))] = -1
        data_dict['User ID'][np.argmax(data_dict['User ID'] == random.choice(
            data_dict['User ID']))] = -101

    # create data frame
    df = pd.DataFrame(data_dict)

    return df