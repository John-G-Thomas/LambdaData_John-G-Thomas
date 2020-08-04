"""
Function cleans dataframe
"""
import pandas as pd


def clean(df):
    df = df.copy()
    # Drop NaN and extra columns and index
    df.dropna(subset=[df.select_dtypes(include=['datetime64'])], inplace=True)
    df.set_index(pd.to_datetime(df.select_dtypes(include=['datetime64'])), inplace=True)
    return df


"""
clean data's and add specific columns# def cleandate(df):
"""


def cleandates(df):
    df = df.copy()
    df['Year'] = (df.select_dtypes(include=['datetime64']).to_period('Y'))
    df['Month'] = (df.select_dtypes(include=['datetime64']).to_period('M'))
    df['Day'] = (df.select_dtypes(include=['datetime64']).to_period('D'))
    return df


def assess_NA(data):
    """
    Returns a pandas dataframe denoting the total number of NA values and the percentage of NA values in each column.
    The column names are noted on the index.

    Parameters
    ----------
    data: dataframe
    """
    # pandas series denoting features and the sum of their null values
    null_sum = data.isnull().sum()  # instantiate columns for missing data
    total = null_sum.sort_values(ascending=False)
    percent = (((null_sum / len(data.index)) * 100).round(2)).sort_values(ascending=False)

    # concatenate along the columns to create the complete dataframe
    df_NA = pd.concat([total, percent], axis=1, keys=['Number of NA', 'Percent NA'])

    # drop rows that don't have any missing data; omit if you want to keep all rows
    df_NA = df_NA[(df_NA.T != 0).any()]

    return df_NA
