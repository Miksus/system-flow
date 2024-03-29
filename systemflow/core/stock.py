
"""

Container for system values.

Stocks can be seen as the storages
for transferable but not copyable
goods/asset/measurement

Examples:
    - Cash
    - Mass
    - 
"""
from systemflow.core.base import SimBase
from systemflow.core import flow
from systemflow.core import computator

from systemflow import exceptions


class Stock(SimBase):
    """[summary]
    
    Examples:
    ---------
        Stock("A") >> Stock("B")
        >>> Flow(input=Stock("A"), output=Stock("B"))

        Stock("A") * 0.2
        >>> Valve(Stock("A"))

    Returns:
        [type] -- [description]
    """
    _sysflow_attrs = ()
    
    def __init__(self, name, initial_value=None, lower_limit=None, upper_limit=None):
        self.name = name

        self.initial_value = initial_value
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

        self.history = []

        self.value = initial_value
    
    def reset(self):
        self.value = self.initial_value

    def isin_limits(self, value):
        lower_ok = (
            value >= self.lower_limit 
            if self.lower_limit is not None 
            else True
        )
        upper_ok = (
            value <= self.upper_limit 
            if self.upper_limit is not None 
            else True
        )
        return lower_ok and upper_ok

    @property
    def allowed_changes(self):
        return (
            self.lower_limit - self.value,
            self.upper_limit - self.value
        )

    def validate_value(self, value=None, increment=None, decrement=None):
        increment = 0 if increment is None else increment
        decrement = 0 if decrement is None else decrement
        orig_value = self.value if value is None else value

        new_value = orig_value + increment - decrement

        if not self.isin_limits(new_value): 

            raise exceptions.OutOfLimitsError(
                lower_limit=self.lower_limit,
                upper_limit=self.upper_limit,
                proposed_value=new_value,
                current_value=self.value
            )

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if isinstance(other, Stock):
            return self.name == other.name
        elif isinstance(other, str):
            return self.name == other

    def __iadd__(self, other):
        "Fill stock"
        # self += other
        new_value = self.value + other
        
        if self.isin_limits(new_value):
            self.value = new_value
        else:
            # Goes over the limits
            raise exceptions.OutOfLimitsError(
                lower_limit=self.lower_limit,
                upper_limit=self.upper_limit,
                proposed_value=new_value,
                current_value=self.value
            )
        return self
        
    def __isub__(self, other):
        "Drain stock"
        # self -= other
        new_value = self.value - other
        
        if self.isin_limits(new_value):
            self.value = new_value
        else:
            # Goes over the limits
            raise exceptions.OutOfLimitsError(
                lower_limit=self.lower_limit,
                upper_limit=self.upper_limit,
                proposed_value=new_value,
                current_value=self.value
            )
        return self

# Extended arithmetics
    def __add__(self, other):
        # self + other
        # >>> Operation(self, other)
        return computator.AddComputator(self, other)

    def __sub__(self, other):
        # self - other
        return computator.SubComputator(self, other)

    def __mul__(self, other):
        # self * other
        return computator.MulComputator(self, other)

    def __truediv__(self, other):
        # self / other
        return computator.DivComputator(self, other)

# Reverse arithmetics
    def __radd__(self, other):
        # other + self
        # >>> Operation(self, other)
        return computator.AddComputator(other, self)

    def __rsub__(self, other):
        # other - self
        return computator.SubComputator(other, self)

    def __rmul__(self, other):
        # other * self
        return computator.MulComputator(other, self)

    def __rtruediv__(self, other):
        # other / self
        return computator.DivComputator(other, self)

# Flow mechanics
    def __rshift__(self, other):
        # self >> other
        if other is None:
            return flow.OutFlow(self)
        else:
            return flow.Flow(input=self, output=other)

    def __rrshift__(self, other):
        # other >> self
        if other is None:
            return flow.InFlow(self)
        else:
            return flow.Flow(input=other, output=self)

    def __lshift__(self, other):
        # self << other
        if other is None:
            return flow.InFlow(self)
        else:
            return flow.Flow(input=other, output=self)

    def __rlshift__(self, other):
        # other << self
        if other is None:
            return flow.OutFlow(self)
        else:
            return flow.Flow(input=self, output=other)

# Display
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Stock({self.name}, value={self.value}, limits=({self.lower_limit}, {self.upper_limit}))'