"""
Function to add date columns from datetime column
"""


def chaindata_date(df: Object) -> Object:
    df['Year'] = df['date_column'].dt.to_period('Y')
    df['Month'] = df['date_column'].dt.to_period('M')
    df['Day'] = df['date_column'].dt.to_period('D')
    return df
