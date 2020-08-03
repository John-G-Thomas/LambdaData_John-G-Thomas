"""
Function get date into int
"""


def get_date_int(df, date_column):
    df["year"] = df[date_column].dt.year
    df["month"] = df[date_column].dt.month
    return year, month, week
