
from collections import Iterable
from systemflow import visuals

class SimBase:

    """
    Base class for all sysflow classes

        _sysflow_attrs [Iterable]: a collection of attribute names that contains SimBase elements
    """
    _timeline = None
    _sysflow_attrs = None
    graphviz = visuals.Graphviz()

    @property
    def timeline(self):
        return self._timeline

    @timeline.setter
    def timeline(self, value):
        "Set timeline to this and all of the composed instances"
        self._timeline = value
        for sysflow_elem in self.sub_elements():

            has_same_value = getattr(sysflow_elem, '_timeline', None) is value
            if not has_same_value:
                attr_val.timeline = value

    def sub_elements(self):
        "Return all SystemFlow elements from the object"
        def yield_sysflow_elems(elem):
            if isinstance(elem, SimBase):
                yield elem
                yield from elem.sub_elements()

        if self._sysflow_attrs is not None:
            # Defining for speed-up (and handling tupled elements)
            for attr_name in self._sysflow_attrs:
                attr = getattr(self, attr_name)

                if isinstance(attr, (tuple, list, set)):
                    # attr must be iterable of 
                    attr_container = attr
                    for attr in attr_container:
                        yield from yield_sysflow_elems(attr)
                else:
                    yield from yield_sysflow_elems(attr)

        else:
            for attr_name, attr in vars(self).items():
                yield from yield_sysflow_elems(attr)

    def reset_all(self):
        "Reset all elements this element has"
        self.reset()
        for elem in self.sub_elements:
            elem.reset()

    def reset(self):
        "Reset this element"
        if hasattr(self, "has_memory") and self.has_memory:
            raise NotImplementedError