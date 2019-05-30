
from collections import Iterable
from systemflow import visuals

class SimBase:

    """
    Base class for all sysflow classes
    """
    _timeline = None
    graphviz = visuals.Graphviz()

    @property
    def timeline(self):
        return self._timeline

    @timeline.setter
    def timeline(self, value):
        "Set timeline to this and all of the composed instances"
        self._timeline = value
        for sysflow_elem in self.sub_elements:

            has_same_value = getattr(sysflow_elem, '_timeline', None) is value
            if not has_same_value:
                attr_val.timeline = value

    @property
    def sub_elements(self):
        "Return all SystemFlow elements from the object"
        return {attr_val for attr, attr_val in vars(self).items() if isinstance(attr_val, SimBase)}

    def reset_all(self):
        "Reset all elements this element has"
        self.reset()
        for elem in self.sub_elements:
            elem.reset()

    def reset(self):
        "Reset this element"
        if hasattr(self, "has_memory") and self.has_memory:
            raise NotImplementedError