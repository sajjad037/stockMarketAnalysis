from api.constants import API_KEY, API_BASE_URL, Exchange, APIFunction, OutputSize
from api.model import MetaData
from datetime import datetime
import requests
import logging


def call_stock_api(exchange: str, symbol: str, function: str, outputsize= str):
    url = f"{API_BASE_URL}?function={function}&symbol={symbol}.{exchange}&outputsize={outputsize}&apikey={API_KEY}"
    print("url: ", url)
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        response_data = response.json()

        # Parse MetaData
        meta_data = parse_meta_data(response_data["Meta Data"])
        del response_data["Meta Data"]

        # Parse Time

        for item in response_data.items():
            print(item)
            print(type(item))
    else:
        logging.error(f"getting status_code:{response.status_code}, for request:{url}")


def parse_meta_data(meta_data: dict):
    return MetaData(
        meta_data["1. Information"],
        meta_data["2. Symbol"],
        datetime.strptime(meta_data["3. Last Refreshed"], '%Y-%m-%d'),
        meta_data["4. Output Size"],
        meta_data["5. Time Zone"]
    )


def parse_time_series_data(time_series_data: dict):
    pass


if __name__ == '__main__':
    call_stock_api(Exchange.LON.name, "TSCO", APIFunction.TIME_SERIES_DAILY_ADJUSTED.value, OutputSize.compact.value)
