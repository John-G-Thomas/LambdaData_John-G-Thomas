"""
Function to add date columns from datetime column
"""

import pandas as pd
import numpy as np
import datetime

    def chaindata_date(df):
        self['Year'] = df['date_column'].dt.to_period('Y')
        self['Month'] = df['date_column'].dt.to_period('M')
        self['Day'] = df['date_column'].dt.to_period('D')
        return df

