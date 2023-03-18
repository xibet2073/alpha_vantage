from alpha_vantage.timeseries import TimeSeries

api_key = "ROMSNL4PGI859X8N"

ts = TimeSeries(key = api_key, output_format = 'csv')

data_csv, _ = ts.get_intraday("IBM", '5min', 'full')
print(type(data_csv))

# for index, row in enumerate(data_csv):
#     print(', '.join(row))

# Save data_csv to intraday.csv
with open('csv/intraday.csv', 'w') as file:
    for row in data_csv:
        file.write(', '.join(row))
        file.write('\n')


