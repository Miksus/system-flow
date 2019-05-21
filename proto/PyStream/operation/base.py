

"""
Operations are group of classes that do not distribute
system's values but do control the flows by turning 
valves in flows

"""


class Operation:


    def __init__(self, *args, func=None):
        self.inputs = args
        self._func = func

    def __iter__(self):
        return self

    def __next__(self):
        "Next value of the operation"
        return self()

    def __call__(self):

        func = self._func
        # Multivalue
        if callable(func):
            if len(self.inputs) > 0:
                return func(self.input_values)
            else:
                return func()

        if len(self.inputs) > 2:
            func_map = {
                "sum": sum
            }
            return func_map[func](self.input_values)
        elif len(self.inputs) == 2:
            # Two values
            method_map = {
                "add": "__add__",
                "sub": "__sub__",
                "mul": "__mul__",
                "div": "__div__"
            }
            method_str = method_map.get(func, func)
            return getattr(self.input_values[0], method_str)(self.input_values[1])
        elif len(self.inputs) == 1:
            attr_str = func
            return getattr(self.inputs[0], attr_str)

    @property
    def input_values(self):
        return [
            input.value if isinstance(input, Stock)
            else input() if isinstance(input, Operation)
            else input if isinstance(input (float, int))
            else None
            for input in self.inputs
        ]

    def __add__(self, other):
        # self + other
        return Operation(self, other, func="add")

    def __sub__(self, other):
        # self - other
        return Operation(self, other, func="sub")

    def __mul__(self, other):
        # self * other
        return Operation(self, other, func="mul")

    def __floordiv__(self, other):
        # self // other
        pass

    def __div__(self, other):
        # self / other
        return Operation(self, other, func="div")