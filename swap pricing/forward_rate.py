# Function to calculate forward rate between two times t1 and t2
def calculate_forward_rate(yield_curve, t1, t2):
    y_t1 = yield_curve.interpolated_yield_curve(t1)
    y_t2 = yield_curve.interpolated_yield_curve(t2)
    forward_rate = (y_t2 * t2 - y_t1 * t1) / (t2 - t1)
    return forward_rate

# Calculate the forward curve for the sample data
forward_curve = [calculate_forward_rate(yield_curve_obj, maturity[i], maturity[i+1]) for i in range(len(maturity) - 1)]

# Since we lose one point due to the pairwise calculation, we'll adjust the maturity array for plotting
maturity_for_forward_curve = (maturity[:-1] + maturity[1:]) / 2
