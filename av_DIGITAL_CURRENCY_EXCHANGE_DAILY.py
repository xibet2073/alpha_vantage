from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

cc = CryptoCurrencies(key = api_key, output_format="pandas")

data = cc.get_digital_currency_daily("BTC", "USD")
print(data)