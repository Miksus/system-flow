

class SimBase:

    """
    Base class for all sysflow classes
    """
    _timeline = None

    @property
    def timeline(self):
        return self._timeline

    @timeline.setter
    def timeline(self, value):
        "Set timeline to this and all of the composed instances"
        self._timeline = value
        for attr, attr_val in vars(self).items():

            is_attr_simbase = isinstance(attr_val, SimBase)
            
            if is_attr_simbase:
                
                has_same_value = getattr(attr_val, '_timeline', None) is value

                if not has_same_value:
                    attr_val.timeline = value


class OperationBase(SimBase):
    pass

class StockBase(SimBase):
    pass

class FlowBase(SimBase):
    pass
