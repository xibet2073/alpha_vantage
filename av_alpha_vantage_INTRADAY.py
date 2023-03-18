from alpha_vantage.timeseries import TimeSeries
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

ts = TimeSeries(key = api_key, output_format = 'pandas')

data, metadata = ts.get_intraday("IBM", '5min', 'full')
print(metadata)

#data.head()
#display(data)
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(data)
