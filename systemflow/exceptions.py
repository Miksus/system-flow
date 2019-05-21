

class OutOfLimitsError(Exception):
    "Value is out of bounds"
    def __init__(self, current_value, proposed_value, lower_limit, upper_limit):
        self.proposed_value = proposed_value
        self.current_value = current_value
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    @property
    def allowed_change(self):
        lower_limit = self.lower_limit
        upper_limit = self.upper_limit
        prop_value = self.proposed_value
        value = self.current_value
        if lower_limit is not None and prop_value < lower_limit:
            return lower_limit - value
        elif upper_limit is not None and prop_value > upper_limit:
            return upper_limit - value

class FlowOver(Exception):
    "Flow is about to flow over limits"
