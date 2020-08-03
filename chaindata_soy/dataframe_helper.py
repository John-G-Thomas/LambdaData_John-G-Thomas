"""
Function to add date columns from datetime column
"""


def get_date_int(df, date_column):
    year = df[date_column].dt.year
    month = df[date_column].dt.month
    week = df[date_column].dt.week
    return year, month, week
