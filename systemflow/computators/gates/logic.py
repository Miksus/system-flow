from systemflow.computators import ComputatorBase

class GateBase(ComputatorBase):
    """
    Base for all Gates

    Gate is a computator subclass that 
    
    
    Arguments:
        ComputatorBase {[type]} -- [description]
    """
    def __init__(self, *inputs):
        

    def process(self, **inputs):
        raise NotImplementedError



class AndGate(GateBase):
    _operation_symbol = " & "
    def process(self, *inputs):
        return all(self.inputs)
    
class OrGate(LogicGateBase):
    _operation_symbol = " | "
    

class Notgate(LogicGateBase):
    _operation_symbol = "~"
    