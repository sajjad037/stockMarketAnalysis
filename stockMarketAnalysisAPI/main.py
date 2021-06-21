from api.constants import API_KEY, API_BASE_URL, Exchange, APIFunction, OutputSize, DATA_FILTER_DAYS, PAST_MAX_LOW_DAYS
from api.model import MetaData, DailyTimeSeries
from datetime import datetime, date, timedelta
import requests
import logging


def call_stock_api(exchange: Exchange, symbol: str, function: APIFunction, output_size: OutputSize):
    if exchange == Exchange.US:
        url = f"{API_BASE_URL}?function={function.value}&symbol={symbol}&outputsize={output_size.value}&apikey={API_KEY}"
    else:
        url = f"{API_BASE_URL}?function={function.value}&symbol={symbol}.{exchange.name}&outputsize={output_size.value}&apikey={API_KEY}"
    print("url: ", url)
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        response_data = response.json()
        if "Error Message" not in response_data:

            # Parse MetaData
            meta_data = parse_meta_data(response_data["Meta Data"])
            del response_data["Meta Data"]

            # Parse Time
            time_series_list = []
            time_series_key = list(response_data.keys())[0]
            for time_series_data in response_data[time_series_key].items():
                time_series_list.append(parse_time_series_data(time_series_data[0], time_series_data[1]))

            # Filter list for FILTER_DAYS
            filtered_time_series_list = []
            start_date = date.today()
            end_date = start_date - timedelta(days=DATA_FILTER_DAYS)
            print("start_date: ", type(start_date), start_date, ", End_Data: ", type(end_date), end_date)
            for count, item in enumerate(time_series_list, start=1):
                if start_date >= item.date.date() >= end_date:
                    filtered_time_series_list.append(item)

            # Sort time_series_list by low value
            low_time_series_list = sorted(filtered_time_series_list, key=lambda x: x.low, reverse=False)
            for count, item in enumerate(low_time_series_list, start=1):
                print(f"count={count}, Date={item.date}, low={item.low}")
                if count == PAST_MAX_LOW_DAYS:
                    break

            # Sort time_series_list by low value
            print(f"-------------------------------------------------------")
            high_time_series_list = sorted(filtered_time_series_list, key=lambda x: x.high, reverse=True)
            for count, item in enumerate(high_time_series_list, start=1):
                print(f"count={count}, Date={item.date}, high={item.high}")
                if count == PAST_MAX_LOW_DAYS:
                    break

        else:
            error_message = response_data["Error Message"]
            logging.error(
                f"getting Error Message: {error_message}, with status_code: {response.status_code}, for request:{url}")
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


def parse_time_series_data(date_key: str, time_series_data: dict):
    return DailyTimeSeries(
        datetime.strptime(date_key, '%Y-%m-%d'),
        float(time_series_data["1. open"]),
        float(time_series_data["2. high"]),
        float(time_series_data["3. low"]),
        float(time_series_data["4. close"]),
        float(time_series_data["5. adjusted close"]),
        float(time_series_data["6. volume"]),
        float(time_series_data["7. dividend amount"]),
        float(time_series_data["8. split coefficient"]),
    )


if __name__ == '__main__':
    call_stock_api(Exchange.US, "NIO", APIFunction.TIME_SERIES_DAILY_ADJUSTED, OutputSize.compact)
