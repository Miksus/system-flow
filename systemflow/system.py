
from systemflow.core import Flow, Stock, ComputatorBase

import pandas as pd
import matplotlib.pyplot as plt 

class System:

    def __init__(self, *args, start=0, stop=10, step=1):

        sys_elems = set()
        for arg in args:
            sys_elems.add(arg)
            for sub_arg in arg.sub_elements():
                sys_elems.add(sub_arg)
        
        self.stocks = {arg for arg in sys_elems if isinstance(arg, Stock)}
        self.flows = {arg for arg in sys_elems if isinstance(arg, Flow)}

        self.computators = {arg for arg in sys_elems if isinstance(arg, ComputatorBase)}

        self.all_elems = sys_elems

        self.start = start
        self.stop = stop
        self.step = step

    def simulate(self):
        for elem in self.all_elems:
            elem.reset()
        stock_results = []
        flow_results = []
        comp_results = []
        for state in range(self.start, self.stop, self.step):
            for flow in self.flows:
                flow()

            stock_results.append({
                stock: stock.value
                for stock in self.stocks
            })

            flow_results.append({
                flow: flow.value
                for flow in self.flows
            })

            comp_results.append({
                comp: comp.value
                for comp in self.computators
            })
        self.results = dict(
            flow=pd.DataFrame(flow_results),
            stock=pd.DataFrame(stock_results),
            computator=pd.DataFrame(comp_results)
        )
    
    @property
    def flow_results(self):
        return 

    def plot(self):
        flows = self.results["flow"]
        stocks = self.results["stock"]
        computators = self.results["computator"]

        flows.columns = flows.columns.map(lambda col: str(col))
        stocks.columns = stocks.columns.map(lambda col: str(col))
        computators.columns = computators.columns.map(lambda col: str(col))


        fig, (ax_stocks, ax_flows, ax_comps) = plt.subplots(3, 1, figsize=[10, 20])

        for col in stocks.columns:
            ax_stocks.plot(stocks.index, stocks[col].values, label=col[:30])
        ax_stocks.set_title("Stocks")

        for col in flows.columns:
            ax_flows.plot(flows.index, flows[col].values, label=col[:30])
        ax_flows.set_title("Flows")

        for col in computators.columns:
            ax_comps.plot(computators.index, computators[col].values, label=col[:30])
        ax_comps.set_title("Computators")

        ax_stocks.legend()
        ax_flows.legend()
        ax_comps.legend()


    def __getitem__(self, value):
        if isinstance(value, Stock):
            return next(stock for stock in self.stocks if stock == value)
        elif isinstance(value, Flow):
            return next(flow for flow in self.flows if flow == value)
        else:
            raise NotImplementedError