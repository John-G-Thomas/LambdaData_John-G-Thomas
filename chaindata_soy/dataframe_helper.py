"""
Function cleans dataframe
"""
class cleaned

def cleaned(df):
    df = df.copy()
    # Drop NaN and extra columns and index
    df.dropna(subset=["Datetime"], inplace=True)
    df.set_index(pd.to_datetime(df['Datetime']), inplace=True)
    df.drop('Datetime', axis=1, inplace=True)
    return df


"""
clean datas and add pecific columns# def cleandate(df):
"""
def date(df):
    df df.copy()
    df['Year'] = pd.DatetimeIndex(df['Datetime']).year
    df['Month'] = pd.DatetimeIndex(df['Datetime']).month
    df['Day'] = pd.DatetimeIndex(df['Datetime']).day
    return df
