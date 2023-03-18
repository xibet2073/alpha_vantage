import requests

api_key = 'ROMSNL4PGI859X8N'
function = 'EARNINGS'
symbol = 'IBM'

# Aggiungi il contenuto di requests.get() a df
url = "https://www.alphavantage.co/query?" + \
      "function=" + function + \
      "&symbol=" + symbol + \
      "&apikey=" + api_key

data = requests.get(url).json()
print(data)