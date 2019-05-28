
from collections import Iterable
from systemflow.visuals import Graphviz

class SimBase:

    """
    Base class for all sysflow classes
    """
    _timeline = None
    graphviz = Graphviz()

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


class StockBase(SimBase):
    pass

class FlowBase(SimBase):
    pass


class ContainerMixin(SimBase):

    _allowed_types = None
    _element_name = 'Element'

    def __init__(self, *elems, name=None):
        self.elements = elems
        self.name = name

    def __getitem__(self, key):
        # self[key]
        # Should raise TypeError if type of the key is wrong
        # Should raise KeyError if no corresponding value for the key
        # Should raise IndexError if value not in suitable range

        if isinstance(key, str):
            val = [elem for elem in self.elements if elem.name == key]
            if len(val) > 1:
                raise KeyError(f"Multiple valid names found. Use {self.__class__.__name__}[[{key}]] to get them.")
            return val[0]
        elif isinstance(key, Iterable):
            return [elem for elem in self.elements if elem.name in key]
        elif isinstance(key, int):
            return self.elements[key]
        else:
            raise TypeError(f"Invalid key type: {type(key)}")

    def __setitem__(self, key, value):
        # self[key] = value
        # Should raise TypeError if type of the key is wrong
        # Should raise KeyError if no corresponding value for the key
        # Should raise IndexError if value not in suitable range
        self.elements[key] = value
        raise NotImplementedError

    def __delitem__(self, key):
        # del self[key]
        # Raise KeyError or IndexError or similar if not appropritate
        raise NotImplementedError

    def __len__(self):
        return len(self.elements)

    @property
    def elements(self):
        return self._elems

    @elements.setter
    def elements(self, elements):
        elems = []
        for elem in elements:

            if not isinstance(elem, self._allowed_types):
                raise TypeError(f"All must be in {', '.join([cls.__name__ for cls in self._allowed_types])}. Given: {type(elem).__name__}")

            elems.append(elem)

        self._elems = elems

    def flatten(self):
        for elem in self.elements:
            if isinstance(elem, ContainerMixin):
                yield from elem.flatten()
            else:
                yield elem