from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

cc = CryptoCurrencies(key = api_key)

data = cc.get_digital_currency_exchange_rate("BTC", "USD")
print(data)