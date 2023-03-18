from alpha_vantage.foreignexchange import ForeignExchange
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

fe = ForeignExchange(key = api_key, output_format="pandas")

data, meta_data = fe.get_currency_exchange_daily("EUR", "USD", outputsize="compact")
data.head()


