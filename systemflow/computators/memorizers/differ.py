
from .base import Memorizer

class Differ(Memorizer):
    """
    Memorize the previous value and return 
    the change compared to current value

    Example cases:
    --------------
        Getting profit/loss from last day
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.memory = []

    def process(self, *input_values):
        "Next value of the operation"
        out = [curr - prev for curr, prev in zip(input_values, self.memory)]
        self.memory = input_values
        return out

    def reset(self):
        self.memory = []