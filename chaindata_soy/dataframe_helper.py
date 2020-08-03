"""
Function cleans dataframe
"""


def clean(df):
    df = df.copy()
    # Drop NaN and extra columns and index
    df.dropna(subset=[column], inplace=True)
    df.set_index(pd.to_datetime(df['Datetime']), inplace=True)
    df.drop('Datetime', axis=1, inplace=True)
    return df


"""
clean datas and add pecific columns# def cleandate(df):
"""
