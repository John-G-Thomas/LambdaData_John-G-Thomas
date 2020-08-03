"""
Function to add date columns from datetime column
"""
import datetime as dt


def chaindata_date(df: dt) -> dt:
    """
    :return: cleaned dates
    :rtype: chaindata_date
    :type df: datetime as dt
    """
    df['Year'] = df['date_column'].dt.to_period('Y')
    df['Month'] = df['date_column'].dt.to_period('M')
    df['Day'] = df['date_column'].dt.to_period('D')
    assert isinstance(df, __class_or_tuple=dt.datetime)
    return dt
