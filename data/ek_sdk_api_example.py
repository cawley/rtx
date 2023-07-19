import eikon as ek

ek.set_app_key("YOUR_APP_KEY")  # replace with your app key

df, err = ek.get_data(
    ["AAPL.O", "MSFT.O"],
    ["TR.PriceClose", "TR.Volume"],
    {"SDate": "2017-01-01", "EDate": "2017-12-31", "Frq": "M"},
)

print(df)

# here we use get_data to get data from eikon
