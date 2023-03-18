from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

api_key = "ROMSNL4PGI859X8N"

ts = TimeSeries(key = api_key, output_format = 'pandas')

data, metadata = ts.get_intraday("IBM", '5min', 'full')

sns.set_style("darkgrid")
sns.set_context("notebook")
data.describe()
data['4. close'].plot(figsize=(10, 8))