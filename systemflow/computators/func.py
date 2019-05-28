from .base import ComputatorBase

class Functioner(ComputatorBase):

    def __init__(self, *args, function:callable):
        if not callable(function):
            raise TypeError(f"{function} must be callable")
        if not isinstance(function, callable)
        super().__init__(*args)
        self.func = function

    def process(self, *inputs):
        return self.func(*args)

        