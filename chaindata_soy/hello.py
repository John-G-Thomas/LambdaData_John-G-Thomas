class chaindata_soy
    def chaindata_date(self):
        self['Year'] = df['date_column'].dt.to_period('Y')
        self['Month'] = df['date_column'].dt.to_period('M')
        self['Day'] = df['date_column'].dt.to_period('D')
         return self