
from collections.abc import Iterable

from systemflow.base import FlowBase, StockBase

from systemflow import exceptions
from systemflow.flow import group

class Flow(FlowBase):
    """Flow 
    """

    def __init__(self, input, output, valve=0, at_limit="to limits"):
        """[summary]
        
        Arguments:
            input {Stock} -- Stock to drain
            output {Stock} -- Stock to fill
            valve {[type]} -- Flow value controller
            at_limit {str} -- ({'ignore', 'raise', 'shut', 'to limits'})
        
        Raises:
            TypeError: [description]
        """

        self.input = input
        self.output = output

        self.valve = valve
        self.at_limit = at_limit

    def __call__(self):
        "Flow from input to output by value defined by valve"
        flow_value = self.get_flow_value()

        try:
            self.input.validate_value(decrement=flow_value)
        except exceptions.OutOfLimitsError as err:
            flow_value = -self._get_float_value_error(flow_value, err)

        try:
            self.output.validate_value(increment=flow_value)
        except exceptions.OutOfLimitsError as err:
            flow_value = self._get_float_value_error(flow_value, err)

        self.input -= flow_value
        self.output += flow_value

        self.flow_value = flow_value

    def get_flow_value(self):
        """Value to flow from input to output
        """
        valve = self.valve
        if isinstance(valve, (float, int)):
            flow_val = valve
        elif isinstance(valve, Iterable):
            flow_val = next(valve)
        else:
            raise NotImplementedError(f"Flow value for valve type {type(valve)} not implemented")
        return flow_val 

    def _get_float_value_error(self, flow_value, error):
        "Get float value when error has occured during validating it"
        if self.at_limit == "to limits":
            flow_value = error.allowed_change

        elif self.at_limit == "shut":
            flow_value = 0

        elif self.at_limit == "ignore":
            pass

        elif self.at_limit == "raise":
            raise exceptions.FlowOver()

        else:
            raise NotImplementedError

        return flow_value

    def check_input(self, drain_value):
        new_input_value = self.input.value - drain_value
        return self.input.isin_limits(new_input_value)

    def check_output(self, fill_value):
        new_output_value = self.output.value + fill_value
        return self.output.isin_limits(new_output_value)

    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        if isinstance(value, StockBase):
            self._input = value
        else:
            raise NotImplementedError(type(value))

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        if isinstance(value, StockBase):
            self._output = value
        else:
            raise NotImplementedError
            
    def __repr__(self):
        repr_input = repr(self.input)
        repr_output = repr(self.output)
        repr_valve = repr(self.valve)
        return f'Flow({repr_input} --({repr_valve})--> {repr_output})'

# Alchemy
    def __rshift__(self, other):
        # self >> other
        second_flow = Flow(self.output, other)
        return group.FlowGroup(self, second_flow)

    def __rrshift__(self, other):
        # other >> self
        second_flow = Flow(other, self.input)
        return group.FlowGroup(self, second_flow)