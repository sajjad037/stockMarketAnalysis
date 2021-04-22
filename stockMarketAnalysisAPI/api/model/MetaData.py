import datetime
from datetime import date
from enum import Enum
from typing import Any, Dict, List, Optional, Type, Union


class MetaData:
    def __init__(self, information:str , symbol: str, last_refreshed: date, output_size: str, time_zone: str):
        self.information = information
        self.symbol = symbol
        self.last_refreshed = last_refreshed
        self.output_size = output_size
        self.time_zone = time_zone

    def __str__(self):
        return f"MetaData(information={self.information}, symbol={self.symbol}, " \
               f"last_refreshed={self.last_refreshed}, output_size={self.output_size}, " \
               f"time_zone={self.time_zone})'"


class DailyTimeSeries:
    def __init__(self, date: datetime, open: float, high: float, low: float, close: float, adjusted_close: float,
                 volume: float, dividend_amount: float, split_coefficient: float):
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.adjusted_close = adjusted_close
        self.volume = volume
        self.dividend_amount = dividend_amount
        self.split_coefficient = split_coefficient

    def __str__(self):
        return f"DailyTimeSeries(date={self.date}, open={self.open}, " \
               f"high={self.high}, low={self.low}, " \
               f"close={self.close}, adjusted_close={self.adjusted_close}, " \
               f"volume={self.volume}, dividend_amount={self.dividend_amount}, " \
               f"split_coefficient={self.split_coefficient})'"

#
# class DailyTimeSeriesData:
#     def __init__(self, meta_data: MetaData, time_series_data: List[DailyTimeSeries]):
#         self.meta_data = meta_data
#         self.time_series_data = time_series_data
