#!/usr/bin/env python3

import requests

class AlphaVantage(object):
    def __init__ (self, ticker, api_key):
        self.ticker = ticker.upper()
        self.key = api_key.upper()

    def __str__ (self):
        return f'Ticker Symbol: {self.ticker}'

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

        if function == 'TIME_SERIES_INTRADAY':
            query = {'function': function,
                    'symbol': self.ticker,
                    'interval': interval,
                    'outputsize': outputsize,
                    'apikey': self.api_key}
            return self.get_data(query)

        else if function == 'TIME_SERIES_DAILY':
            query = {'function': function,
                    'symbol': self.ticker,
                    'outputsize': outputsize,
                    'apikey': self.api_key}
        else if function == 'TIME_SERIES_WEEKLY':
            query = {'function': function,
                    'symbol': self.ticker,
                    'apikey': self.api_key}
        else if function == 'TIME_SERIES_MONTHLY':
            query = {'function': function,
                    'symbol': self.ticker,
                    'apikey': self.api_key}
        else:
            raise SymbolException('Invalid Time Series function')
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

    def get_sector(self):
        '''
        Retrives sector data.
        http://www.alphavantage.co/documentation/#sector-information

        Usage:
            symbol.get_sector()

            symbol: a Symbol object
        '''
        query = {'function': 'SECTOR',
                'apikey': self.api_key}

        return self.get_data(query)

    def get_data(self, query):
        '''
        Internal function to get and parse data from the AlphaVantage API

        Usage:
            symbol.get_data(query)

            symbol: a Symbol object
            query: a properly formatted string for the API query
                e.g. 'function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo'
        '''
        url = 'http://www.alphavantage.co/query'

        response = requests.get(url, params=query)
        data = response.json()

        return data

class SymbolException(Exception):
    pass

