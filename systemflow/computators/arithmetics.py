
from systemflow import computators

# Arithmetic
class AddOperation(computators.Operation):
    _operation_symbol = ' + '
    def process(self, val_1, val_2):
        return val_1 + val_2


class SubOperation(computators.Operation):
    _operation_symbol = ' - '
    def process(self, val_1, val_2):
        return val_1 - val_2


class MulOperation(computators.Operation):
    _operation_symbol = ' * '
    def process(self, val_1, val_2):
        return val_1 * val_2


class DivOperation(computators.Operation):
    _operation_symbol = ' / '
    def process(self, val_1, val_2):
        return val_1 / val_2

