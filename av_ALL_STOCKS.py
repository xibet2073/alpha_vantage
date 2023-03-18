import pandas as pd

import csv
import requests

api_key = 'ROMSNL4PGI859X8N'
function = 'LISTING_STATUS'
symbol = 'AAPL'
topics = "technology"
# Aggiungi il contenuto di requests.get() a df
url = "https://www.alphavantage.co/query?" + \
      "function=" + function + \
      "&symbol=" + symbol + \
      "&apikey=" + api_key
df = pd.read_csv(url)
df.head()
