"""
Memorizer base

Memorizers are subclass of Computators that use old values in generation of current value
This should be only computator class that is time agnostic
"""

from systemflow.computators import ComputatorBase

class Memorizer(ComputatorBase):

    def reset(self):
        "Reset to original state"
        raise NotImplementedError