import eikon as ek
import pandas as pd

# Set your Eikon API key
ek.set_app_key('your_app_key')

# Define the RIC for 10-year US Treasury bonds
ric = 'US10YT=RR'

# define field (this example has close price)
fields = ['CLOSE']

# fetch historical data
df, err = ek.get_data(ric, fields)

# port 2 csv
df.to_csv('10_year_treasury_prices.csv')
