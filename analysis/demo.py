import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

traded_prices = [(1, 100), (2, 110), (3, 115), (4, 118), (5, 120)]

df = pd.DataFrame(traded_prices, columns=["Time", "Price"])

# generate the forward curve by calculating the difference between successive prices
df["Forward"] = df["Price"].diff()

# fill the first forward value with the first price
df.loc[0, "Forward"] = df.loc[0, "Price"]

# we can now create an interpolated forward curve with more granularity
f = interp1d(df["Time"], df["Forward"], kind="cubic")

# this time array has thousandth resolution
new_time = np.linspace(df["Time"].min(), df["Time"].max(), 1000)

# here, f interpolates forward prices
new_forward = f(new_time)

# from this we make the new forward curve dataframe
new_df = pd.DataFrame({"Time": new_time, "Forward": new_forward})

# here we plot th epandas dataframe
new_df.plot(x="Time", y="Forward", kind="line")

print(new_df)

plt.show()
