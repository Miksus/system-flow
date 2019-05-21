

"""
Operations are group of classes that do not distribute
system's values but do control the flows by turning 
valves in flows

"""

from systemflow.base import OperationBase, SimBase
from systemflow import computators

class Operation(OperationBase):

    _operation_symbol = ', '

    def __init__(self, *inputs):
        self.inputs = inputs

    def __iter__(self):
        return self

    def __next__(self):
        "Next value of the operation"
        return self()

    def __call__(self):
        values = self.pre_process(*self.inputs)
        return self.process(*values)

    def pre_process(self, *inputs):
        return [
            input() if isinstance(input, Operation)
            else input.value if isinstance(input, SimBase) and hasattr(input, "value")
            else input if isinstance(input (float, int))
            else None
            for input in inputs
        ]

    def __add__(self, other):
        # self + other
        return operation.AddOperation(self, other)

    def __sub__(self, other):
        # self - other
        return operation.SubOperation(self, other)

    def __mul__(self, other):
        # self * other
        return operation.MulOperation(self, other)

    def __div__(self, other):
        # self / other
        return operation.DivOperation(self, other)

    def __str__(self):
        str_inputs = self._operation_symbol.join(
            map(str, self.inputs)
        )
        return f'({str_inputs})'

    def __repr__(self):
        str_inputs = ', '.join(
            map(repr, self.inputs)
        )
        cls_name = self.__class__.__name__
        return f'{cls_name}({str_inputs})'




