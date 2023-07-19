import eikon as ek
import pandas as pd

# access with API key
ek.set_app_key("your_app_key")

# ric for 10yr bonds
# ric is refinitiv id code
ric = "US10YT=RR"

# define field (this example has close price)
fields = ["CLOSE"]

# fetch historical data
df, err = ek.get_data(ric, fields)

# port 2 csv
df.to_csv("10_year_treasury_prices.csv")

# EXPLANATION:
# gets the closing price of 10-year US Treasury bonds and saves it to a .csv file
# https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python
# this is the complete data library for python development with refinitiv
