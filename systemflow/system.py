from collections.abc import Iterable

from systemflow.core import Flow, Stock, ComputatorBase

import pandas as pd
import numpy as np
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
        stock_results = [{
            stock: stock.initial_value 
            for stock in self.stocks
        }]
        flow_results = [{
            flow: np.nan
            for flow in self.flows
        }]
        comp_results = [{
            comp: np.nan
            for comp in self.computators
        }]
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

    def plot(self, stocks:bool = None, flows:bool = None, computators:bool = None):
        to_plot = []
        no_args_defined = stocks is None and flows is None and computators is None

        if stocks or no_args_defined:
            to_plot.append(("Stocks", self.results["stock"]))
        if flows:
            to_plot.append(("Flows", self.results["flow"]))
        if computators:
            to_plot.append(("Computators", self.results["computator"]))

        fig, axes = plt.subplots(len(to_plot), 1, figsize=[10, 7*len(to_plot)])
        axes = [axes] if not isinstance(axes, Iterable) else axes

        for (plot_name, data), ax in zip(to_plot, axes):
            data.columns = data.columns.map(lambda col: str(col))

            for col in data.columns:
                ax.plot(data.index, data[col].values, label=col[:30])

            ax.set_title(plot_name)
            ax.legend()
            ax.set_xlabel("Time")
            ax.axvline(0, color="k", linestyle="--")
        return fig, axes



    def __getitem__(self, value):
        if isinstance(value, Stock):
            return next(stock for stock in self.stocks if stock == value)
        elif isinstance(value, Flow):
            return next(flow for flow in self.flows if flow == value)
        else:
            raise NotImplementedError