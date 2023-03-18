from alpha_vantage.fundamentaldata import FundamentalData
import pandas as pd

api_key = "ROMSNL4PGI859X8N"

fd = FundamentalData(key = api_key)

data = fd.get_company_overview("IBM")

print(data)
#display(data)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(data)
