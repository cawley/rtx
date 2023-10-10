class YieldCurve:
    def __init__(self, maturity, yield_rates):
        self.maturity = maturity
        self.yield_rates = yield_rates
        self.interpolated_yield_curve = CubicSpline(self.maturity, self.yield_rates)
    
    def get_discount_factor(self, time):
        yield_at_time = self.interpolated_yield_curve(time)
        discount_factor = np.exp(-yield_at_time * time)
        return discount_factor

# Test the YieldCurve class
yield_curve = YieldCurve(maturity, yield_rates)
yield_curve.get_discount_factor(1)  # Should return the discount factor for 1 year

