from enum import Enum

API_BASE_URL = "https://www.alphavantage.co/query"
API_KEY = "75GZO8O8MZB9PBJM"


class OutputSize(Enum):
    compact = 'compact'
    full = 'full'


class APIFunction(Enum):
    TIME_SERIES_INTRADAY = 'TIME_SERIES_INTRADAY'
    TIME_SERIES_DAILY_ADJUSTED = 'TIME_SERIES_DAILY_ADJUSTED'
    TIME_SERIES_MONTHLY = 'TIME_SERIES_MONTHLY'
    TIME_SERIES_DAILY= 'TIME_SERIES_DAILY'


class Exchange(Enum):
    TRT = 'Toronto Stock Exchange'
    TRV = 'Toronto Venture Exchange'
    LON = 'London Stock Exchange'
    DEX = 'XETRA'
    BSE = 'BSE'
    SHH = 'Shanghai Stock Exchange'
    SHZ = 'Shenzhen Stock Exchange'
