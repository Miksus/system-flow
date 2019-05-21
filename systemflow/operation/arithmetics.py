
from systemflow import operation

# Arithmetic
class AddOperation(operation.Operation):
    _operation_symbol = ' + '
    def process(self, val_1, val_2):
        return val_1 + val_2


class SubOperation(operation.Operation):
    _operation_symbol = ' - '
    def process(self, val_1, val_2):
        return val_1 - val_2


class MulOperation(operation.Operation):
    _operation_symbol = ' * '
    def process(self, val_1, val_2):
        return val_1 * val_2


class DivOperation(operation.Operation):
    _operation_symbol = ' / '
    def process(self, val_1, val_2):
        return val_1 / val_2

