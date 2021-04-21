# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from api.constants import API_KEY, API_BASE_URL
from api.model import MetaData
from datetime import datetime
import requests

def call_stock_api(exchange: str, symbol: str, function: str, outputsize= str):
    # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSCO.LON&outputsize=compact&apikey=75GZO8O8MZB9PBJM
    url = f"{API_BASE_URL}?function={function}&symbol={symbol}.{exchange}&outputsize={outputsize}&apikey={API_KEY}"
    print("url: ", url)
    response = requests.get(url, verify=False)
    print(response.status_code)
    response_data = response.json()
    print("response_data:", response_data["Meta Data"])
    meta_data = get_meta_data(response_data["Meta Data"])
    print("meta_data: ", type(meta_data.last_refreshed))
    # for item in response_data.items():
    #     print(item)
    #     print(type(item))

def get_meta_data(meta_data: dict):
    return MetaData(
        meta_data["1. Information"],
        meta_data["2. Symbol"],
        datetime.strptime(meta_data["3. Last Refreshed"], '%Y-%m-%d'),
        meta_data["4. Output Size"],
        meta_data["5. Time Zone"]
    )

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    call_stock_api("LON", "TSCO", "TIME_SERIES_DAILY_ADJUSTED", "compact")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# python3 -m venv virtualenv
# source virtualenv/bin/activate
