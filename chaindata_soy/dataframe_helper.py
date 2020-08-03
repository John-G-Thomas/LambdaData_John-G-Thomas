"""
Function to add date columns from datetime column
"""
import pandas as pd
import datetime as dt


def chaindata_date(df: dt):
    """
    :rtype: object
    :type df: datetime as dt
    """
    df['date_column'] = pd.to_datetime(df['date_column'])
    df['Year'] = df['date_column'].dt.to_period('Y')
    df['Month'] = df['date_column'].dt.to_period('M')
    df['Day'] = df['date_column'].dt.to_period('D')
    assert isinstance(df, __class_or_tuple=dt.datetime)
    return
