import requests

av_url = "https://www.alphavantage.co"
av_query_path = "/query?"

FUNCTION = "TIME_SERIES_INTRADAY"
SYMBOL = "IBM"
INTERVAL = "5min"

request_param_function_name = "function="
request_param_symbol_name = "&symbol="
request_param_interval_name = "&interval="

request_param_apikey_name = "&apikey="
request_param_apikey_value = "ROMSNL4PGI859X8N"

api_url = "".join([av_url, av_query_path,
                  request_param_function_name, FUNCTION,
                  request_param_symbol_name, SYMBOL,
                  request_param_interval_name, INTERVAL,
                  request_param_apikey_name, request_param_apikey_value])

response = requests.get(api_url)
data = response.json()

print(data)