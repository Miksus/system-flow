
from .base import Operation

from collections import deque

class LaggedGate(Operation):
    """
    The value is delayed.

    Example cases:
    --------------
        Getting payment of an invoice (usually 30 days from sending invoice)
    """
    has_memory = True
    
    def __init__(self, *args, **kwargs, lag=None):
        super().__init__(*args, **kwargs)
        self.lag = lag
        self._countdown = lag
        self.lagged_values = deque()

    def __next__(self):
        "Next value of the operation"
        self.lagged_values.append(
            super().__call__()
        )
        if self:
            return self.lagged_values.popleft()
        else:
            self._countdown -= 1

    def __bool__(self):
        return bool(self._countdown)
