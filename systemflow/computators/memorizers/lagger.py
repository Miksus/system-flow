
from collections import deque
from .base import Memorizer


class Lagger(Memorizer):
    """
    The value is delayed.

    Example cases:
    --------------
        Getting payment of an invoice (usually 30 days from sending invoice)
    """
    
    def __init__(self, *args, lag=1, **kwargs):
        super().__init__(*args, **kwargs)
        self.lag = lag
        self._countdown = lag
        self.memory = deque()

    def process(self, *input_values):
        "Next value of the operation"
        self.memory.append(input_values)
        if self:
            return self.memory.popleft()
        else:
            self._countdown -= 1

    def __bool__(self):
        return bool(self._countdown)

    def reset(self):
        self._countdown = self.lag
        self.memory = deque()