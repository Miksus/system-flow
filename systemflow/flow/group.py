

"""
Container of similar Flows
Can also enforce the valve to be identical
"""
from systemflow.base import FlowBase, ContainerMixin

class FlowGroup(FlowBase, ContainerMixin):

    _allowed_types = (FlowBase,)
    _element_name = 'flow'

    @property
    def valve(self):
        return self._valve

    @valve.setter
    def valve(self, value):
        "Set common valve"
        for elem in self.elements:
            elem.valve = value

    def __call__(self):
        for flow in self.elements:
            flow()