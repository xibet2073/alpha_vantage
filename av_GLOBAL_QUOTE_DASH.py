import dash as ds
from dash import dash_table
import pandas as pd
import requests

api_key = 'ROMSNL4PGI859X8N'
function = 'GLOBAL_QUOTE'
symbol = 'AAPL'
topics = "technology"
# Aggiungi il contenuto di requests.get() a df
url = "https://www.alphavantage.co/query?" + \
      "function=" + function + \
      "&symbol=" + symbol + \
      "&apikey=" + api_key

data = requests.get(url).json()

df = pd.json_normalize(data)

app = ds.Dash(__name__)

# Imposta l'elemento del layout dell'app
app.layout = dash_table.DataTable(
    id='quote-table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server()