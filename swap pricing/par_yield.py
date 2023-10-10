import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Define the original YieldCurve class based on the uploaded code
class YieldCurve:
    def __init__(self, maturity, yield_rates):
        self.maturity = maturity
        self.yield_rates = yield_rates
        self.interpolated_yield_curve = CubicSpline(self.maturity, self.yield_rates)
    
    def get_discount_factor(self, time):
        yield_at_time = self.interpolated_yield_curve(time)
        discount_factor = np.exp(-yield_at_time * time)
        return discount_factor

# Function to calculate par yield for a given maturity
def calculate_par_yield(yield_curve, maturity):
    if maturity < 1:
        time_periods = np.linspace(0, maturity, int(maturity * 12) + 1)  # Monthly payments for less than 1 year
    else:
        time_periods = np.linspace(0, maturity, int(maturity * 2) + 1)  # Semi-annual payments for 1 year or more
    time_periods = time_periods[1:]  # Remove the first element which is zero
    discount_factors = [yield_curve.get_discount_factor(time) for time in time_periods]
    avg_discount_factor = np.mean(discount_factors)
    par_yield = 1 / avg_discount_factor  # Assuming coupon payment C=1
    return par_yield

# Generate some sample spot curve data
maturity = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0])
yield_rates = np.array([0.01, 0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.045, 0.05, 0.055])

# Create a YieldCurve object
yield_curve_obj = YieldCurve(maturity, yield_rates)

# Calculate the par yield curve
par_yield_curve = [calculate_par_yield(yield_curve_obj, mat) for mat in maturity]

# Plot the par yield curve
plt.figure(figsize=(10, 5))
plt.plot(maturity, par_yield_curve, marker='o', label='Par Yield Curve')
plt.xlabel('Maturity (Years)')
plt.ylabel('Par Yield')
plt.title('Par Yield Curve')
plt.legend()
plt.grid(True)
plt.show()