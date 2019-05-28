

"""
Computators are group of classes that do not distribute
system's values but do control the flows by turning 
valves their valves.

"""
import inspect
from typing import List, Tuple

from systemflow.base import SimBase
from systemflow import computators
from systemflow.utils import list_of_lists

class ComputatorBase(SimBase):

    """
    Computator base for all classes that
    do not change affect directly to the
    stocks but via valves.

    Can be viewed as electronical signals
    in a water management
    """

    _operation_symbol = ', '

    def __init__(self, *inputs):
        self.inputs = inputs

    @property
    def inputs(self):
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):

        self._validate_arg_count(inputs, method_name="process")
        self._inputs = inputs


    def _validate_arg_count(self, args, method_name):
        "Validate that arguments match to the required amount in the method"
        sig = inspect.signature(getattr(self, method_name))
        param_kinds = [param.kind for param in sig.parameters.values()]

        has_unlimited_args = inspect.Parameter.VAR_POSITIONAL in param_kinds
        arg_amount_ok = len(args) == len(param_kinds)

        if has_unlimited_args or arg_amount_ok:
            # All OK
            return None
        else:
            raise TypeError(
                f"{self.__class__.__name__} method '{method_name}'" 
                f" takes only {len(param_kinds)} inputs. Given: {len(inputs)}"
            )


    def __iter__(self):
        return self

    def __next__(self):
        "Next value of the operation"
        return self()

    def __call__(self):
        """Execute Computators
        Calls all sub computators and  """
        values = self.ignite_inputs(*self.inputs)
        values = self.pre_process(*values)
        return self.process(*values)

    def ignite_inputs(self, *inputs) -> List[float]:
        "Transform the input types for computing"
        return [
            input_ if isinstance(input_, (float, int))
            else input_.value if isinstance(input_, SimBase) and hasattr(input_, "value")
            else input_() if isinstance(input_, ComputatorBase)
            else None
            for input_ in inputs
        ]

    def pre_process(self, *input_values):
        "Flat input values: list of list (of list...) to list"
        return list_of_lists.flatten(input_values)


    def process(self, *input_values: Tuple[float]) -> float:
        "Calculate the inputs accordingly"
        raise NotImplementedError(f"Process not implemented for {self.__class__.__name__}")

    def __add__(self, other):
        # self + other
        return AddComputator(self, other)

    def __sub__(self, other):
        # self - other
        return SubComputator(self, other)

    def __mul__(self, other):
        # self * other
        return MulComputator(self, other)

    def __div__(self, other):
        # self / other
        return DivComputator(self, other)

    def __str__(self):
        str_inputs = self._operation_symbol.join(
            map(str, self.inputs)
        )
        return f'({str_inputs})'

    def __repr__(self):
        str_inputs = self._operation_symbol.join(
            map(repr, self.inputs)
        )
        cls_name = self.__class__.__name__
        return f'{cls_name}({str_inputs})'


# Arithmetic
class AddComputator(ComputatorBase):
    _operation_symbol = ' + '
    _max_inputs = 2
    def process(self, val_1, val_2):
        return val_1 + val_2


class SubComputator(ComputatorBase):
    _operation_symbol = ' - '
    def process(self, val_1, val_2):
        return val_1 - val_2


class MulComputator(ComputatorBase):
    _operation_symbol = ' * '
    def process(self, val_1, val_2):
        return val_1 * val_2


class DivComputator(ComputatorBase):
    _operation_symbol = ' / '
    def process(self, val_1, val_2):
        return val_1 / val_2
