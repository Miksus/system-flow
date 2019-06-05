#from graphviz import Digraph, Source

#from .flow import flow_to_source, flow_to_source_simple
#from .stock import stock_to_source
#from .computator import computator_to_source

try:
    from graphviz import Digraph, Source
except ModuleNotFoundError:
    raise
    import warnings
    warnings.warn("Graphviz not found. Cannot display diagrams.", category=ImportWarning)

from systemflow import core

class Graphviz:
    """Attribute class for plotting Graphviz and getting Graphviz source

    Usage:
    class ExampleClass:
        graphviz = Graphviz()

    myobj = ExampleClass()
    myobj.graphviz.plot()
    """
    stock_shape = "box3d"
    stock_fillcolor = "lightblue2"

    def __init__(self, source=None):
        if source is not None:
            self.source = source

    
    def __get__(self, instance, owner):
        "Backdoor to this class"
        # instance.self
        # where self is CLASS attribute of owner
        # and instance is instance of owner class
        mapping = {
            core.stock.Stock: self.stock_to_source,
            core.flow.Flow: self.flow_to_source,
            core.computator.ComputatorBase: self.computator_to_source
        }

        for base_cls, func in mapping.items():
            if isinstance(instance, base_cls):
                src = func(instance)
                return Graphviz(src)
        else:
            raise NotImplementedError(owner)


    def __set__(self, instance, value):
        # instance.self = value
        # where self is CLASS attribute
        pass

    def __str__(self):
        return self.source

    @property
    def graph_obj(self):
        "Return Graphviz graph object"
        src = 'digraph {' + str(self) + '}'
        return Source(src)

    def _repr_svg_(self):
        src = 'digraph {' + str(self) + '}'
        return Source(src)._repr_svg_()

    @staticmethod
    def stock_to_source(*stocks):
        node_sources = (
            Graphviz.to_node(
                stock, 
                shape=Graphviz.stock_shape, 
                fillcolor=Graphviz.stock_fillcolor,
                 style="filled"
            ) for stock in stocks
        )
        return ''.join(node_sources)

    @staticmethod
    def flow_links_to_source(*flows):
        edge_sources = (
            Graphviz.to_link(
                flow.input, 
                flow.output, 
                label=flow.name if hasattr(flow, "name") else ''
            ) 
            for flow in flows
        )

        source = ''.join(edge_sources)
        return source

    @staticmethod
    def flow_to_source(*flows, include_stocks=True):
        
        input_edge_sources = (
            Graphviz.to_link(
                flow.input, 
                flow, 
                label=flow.name if hasattr(flow, "name") else '',
                arrowhead="none"
            ) 
            for flow in flows
        )
        output_edge_sources = (
            Graphviz.to_link(
                flow, 
                flow.output, 
                label=flow.name if hasattr(flow, "name") else ''
            ) 
            for flow in flows
        )
        node_sources = (
            Graphviz.to_node(flow, shape="doublecircle", label="", fixedsize=True, height=.25) 
            for flow in flows
        )

        valve_sources = (Graphviz.valve_to_source(flow) for flow in flows)

        if include_stocks:
            node_sources_stocks = (
                Graphviz.stock_to_source(flow.input) + Graphviz.stock_to_source(flow.output)
                for flow in flows
            )
        else:
            node_sources_stocks = ['']

        source = (
            ''.join(input_edge_sources) 
            + ''.join(output_edge_sources)
            + ''.join(node_sources) 
            + ''.join(node_sources_stocks)
            + ''.join(valve_sources)
        )

        return source

    @staticmethod
    def computator_to_source(comp):
        inputs = comp.inputs
        symb = comp._operation_symbol
        
        label = type(comp).__name__
        
        comp_node = Graphviz.to_node(comp, label=label, shape="point", fillcolor=None)
        body = comp_node
        for input in inputs:

            curr_link = Graphviz.to_link(input, comp, label=symb, style="dotted")

            is_input_computator = isinstance(input, core.computator.ComputatorBase)
            is_input_stock = isinstance(input, core.stock.Stock)
            if is_input_computator:
                sub_sources = Graphviz.computator_to_source(input)
            elif is_input_stock:
                sub_sources = Graphviz.stock_to_source(input)
            else:   
                # When input is int/float/et cetera
                sub_sources = Graphviz.to_node(input, label=str(input), shape="plaintext", fillcolor=None)
    
            body += curr_link + sub_sources
        return body

    @staticmethod
    def valve_to_source(flow):
        valve = flow.valve
        base_source = Graphviz.to_link(valve, flow, style="dashed")

        is_valve_computator = isinstance(valve, core.computator.ComputatorBase)

        if is_valve_computator:
            sub_str = Graphviz.computator_to_source(valve)
            return base_source + ''.join(sub_str)
            
        else:
            return base_source

    @staticmethod
    def to_node(obj, label=None, end=";\n", **kwargs):
        has_obj_name = hasattr(obj, "name")
        has_label_defined = label is not None

        if not has_label_defined and has_obj_name:
            kwargs["label"] = obj.name
        elif has_label_defined:
            kwargs["label"] = label

        if kwargs:
            attrs = ', '.join(f'{key}="{val}"' for key, val in kwargs.items())
            attrs = f'[{attrs}]'
        else:
            attrs = ''

        return f'{id(obj)}{attrs}' + end

    @staticmethod
    def to_link(from_obj, to_obj, end=";\n", **kwargs):
        if kwargs:
            attrs = ', '.join(f'{key}="{val}"' for key, val in kwargs.items())
            attrs = f'[{attrs}]'
        else:
            attrs = ''
        return f'{id(from_obj)} -> {id(to_obj)}{attrs}' + end