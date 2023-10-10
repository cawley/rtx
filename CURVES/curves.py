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

class LegCashFlows(YieldCurve):
    def __init__(self, maturity, yield_rates, notional, rate, frequency):
        super().__init__(maturity, yield_rates)
        self.notional = notional
        self.rate = rate
        self.frequency = frequency
        self.cash_flow_dates = np.arange(self.frequency, maturity_years + self.frequency, self.frequency)
    
    def calculate_cash_flows(self):
        cash_flows = self.notional * self.rate * self.frequency
        return cash_flows
    
    def calculate_present_value(self):
        cash_flows = self.calculate_cash_flows()
        discount_factors = self.get_discount_factor(self.cash_flow_dates)
        present_value = (cash_flows * discount_factors).sum()
        return present_value

# Test the LegCashFlows class
fixed_leg = LegCashFlows(maturity, yield_rates, notional_amount, fixed_rate, 0.5)
fixed_leg_npv_test = fixed_leg.calculate_present_value()
fixed_leg_npv_test  # Should return the NPV for the fixed leg
