
from .flow import Flow
from .timeline import Timeline
class System:

    def __init__(self, *args, start, stop, step=None):
        
        self.stocks = {arg for arg in args if isinstance(arg, Stock)}
        self.flows = {arg for arg in args if isinstance(arg, Flow)}

        operations = {flow.valve for flow in self.flows if isinstance(flow.valve, Operation)}
        for oper in operations:
            operations.add(inp for inp in oper.inputs if isinstance(inp, Operation))
        self.operations = operations

    def append(self, stock):
        self.stocks.append(stock)

    def add_flow(self, input, output=None, **kwargs):
        if isinstance(input, Flow):
            flow = input
        else:
            input_stock = input if isinstance(input, Stock) else self[input]
            output_stock = output if isinstance(output, Stock) else self[output]
            name = self._next_unique_name()
            flow = Flow(input_stock, output_stock, name=name, **kwargs)

        self.flows.append(flow)

    def simulate(self):
        for state in TimeLine(self.start, self.stop, self.step):
            for flow in self.flows:
                flow()

    def _next_unique_name(self):
        name_base, i = "flow {}", 0
        name = name_base.format(i)
        while name in self.flows:
            i += 1
            name = name_base.format(i)
        return name

    def __getitem__(self, value):
        if isinstance(value, Stock):
            return next(stock for stock in self.stocks if stock == value)
        elif isinstance(value, Flow)
            return next(flow for flow in self.flows if flow == value)
        else:
            raise NotImplementedError