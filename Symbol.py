#!/usr/bin/env python3

class Symbol(object):
    def __init__ (self, ticker, api_key):
        self.symbol = ticker
        self.key = api_key

    def __str__ (self):
        return f'Ticker Symbol: {self.symbol}'

    def get_time_series(self, function, outputsize='compact', interval='5min'):
        '''
        Retrives the specified time series data.
        http://www.alphavantage.co/documentation/#time-series-data

        Usage:
            symbol.get_time_series(function[, outputsize[, interval]])

            symbol: a Symbol object
            function: one of 'intraday', 'daily', 'weekly', or 'monthly'
            outputsize: (intraday and daily only) 'compact' (default) or 'full'
            interval: (intraday only) one of '1min', '5min' (default), '15min',
                '30min', or '60min'
        '''
        function = 'TIME_SERIES_' + function.upper()

        if function = ''
        # TODO: finish function

    def get_indicator(self, function, interval, period = 60, series = 'open',
            *args, **kwargs)
        '''
        Retrieves the specified technical indicator data.
        http://www.alphavantage.co/documentation/#technical-indicators

        Usage:
            symbol.get_indicator(function, interval[, period, series, ...])

            symbol: a Symbol object
            function: the technical indicator*
            interval: one of '1min', '5min', '15min', '30min', '60min', 'daily',
                'weekly', or 'monthly'
            period: a positive integer. Not used in some functions*
            series: one of 'close', 'open', 'high', or 'low'. Not used in some
                functions*
            ...: other parameters as needed by the function*

            * See the AcroMetrics documentation for more information.
        '''
        # TODO: finish function

    def parse_data(self, data):
        '''
        Internal function to parse data from get_data()

        Usage:
            symbol.parse_data(data)

            symbol: a Symbol object
            data: a raw JSON object
        '''
        # TODO: parsing. Return Parsed JSON.

    def get_data(self, api_call):
        '''
        Internal function to get data from the AlphaVantage API

        Usage:
            symbol.get_data(api_call)

            symbol: a Symbol object
            api_call: a properly formatted string for the API query
                e.g. 'function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
        '''
        # TODO: get raw JSON, return it.

    def generate_query(self, query):
        '''
        Internal function to generate a query for the AlphaVantage API

        Usage:
            symbol.generate_query(query)

            symbol: a Symbol object
            query: a dictionary with where keys are API parameters and values
                are their values
        '''
        # TODO: return query string from dict of parameters

