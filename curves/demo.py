import pandas as pd
import numpy as np
from scipy.interpolate import interp1d
from matplotlib import pyplot as plt

traded_prices = [(1, 100), (2, 110), (3, 115), (4, 118), (5, 120)]

df = pd.DataFrame(traded_prices, columns=['Time', 'Price'])

# generate the forward curve by calculating the difference between successive prices
df['Forward'] = df['Price'].diff()

# fill the first forward value with the first price
df.loc[0, 'Forward'] = df.loc[0, 'Price']

# We can now create an interpolated forward curve with more granularity
# First, define the function that will be used for interpolation
f = interp1d(df['Time'], df['Forward'], kind='cubic')

# Now, we can generate a more granular time array
new_time = np.linspace(df['Time'].min(), df['Time'].max(), 1000)

# Use the function to interpolate the forward prices
new_forward = f(new_time)

# We can now construct the new forward curve DataFrame
new_df = pd.DataFrame({
    'Time': new_time,
    'Forward': new_forward
})

new_df.plot(x='Time', y='Forward', kind='line')

print(new_df)

plt.show()
