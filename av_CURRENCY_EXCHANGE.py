from alpha_vantage.foreignexchange import ForeignExchange
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

fe = ForeignExchange(key = api_key)

data = fe.get_currency_exchange_rate("EUR", "USD")
print(data)