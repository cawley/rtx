from twelvedata import TDClient

# Initialize client - apikey parameter is requiered
td = TDClient(apikey="YOUR_API_KEY_HERE")

# Construct the necessary time series
ts = td.time_series(
    symbol="AAPL",
    interval="1min",
    outputsize=10,
    timezone="America/New_York",
)

# Returns pandas.DataFrame
ts.as_pandas()
