from alpha_vantage.techindicators import TechIndicators
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

ti = TechIndicators(key = api_key, output_format = "pandas")

# Weighted Moving Average (WMA)
data, meta_data = ti.get_wma(symbol = "AAPL", interval = "60min", time_period=60)
data.head(10)