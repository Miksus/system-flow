

"""
Container of similar Flows
Can also enforce the valve to be identical
"""


from systemflow.core import group
from systemflow.core import flow

class FlowGroup(group.ContainerMixin):

    _allowed_types = (flow.Flow,)
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