

import pytest

import systemflow as sf


def test_core_diag_no_error():

    stock = sf.Stock("A")
    stock_b = sf.Stock("B")
    stock_c = sf.Stock("C")

    flow = sf.Flow(stock, stock_b)
    flow_b = sf.Flow(stock_b, stock_c)

    stockgroup = sf.StockGroup(stock, stock_b)
    stockgroup_nested = sf.StockGroup(stockgroup, sf.Stock("C"))

    flowgroup = sf.FlowGroup(flow, flow_b)
    computator = sf.core.computator.ComputatorBase()

    # Testing
    stock_diag = stock.graphviz
    flow_diag = flow.graphviz
    comp_diag = computator.graphviz

    for diag in (stock_diag, flow_diag, comp_diag):
        diag._repr_svg_()
        assert isinstance(diag.source, str)
        assert diag.source != ''
    
    

def test_group_source_no_error():

    stock = sf.Stock("A")
    stock_b = sf.Stock("B")
    stock_c = sf.Stock("C")

    flow = sf.Flow(stock, stock_b)
    flow_b = sf.Flow(stock_b, stock_c)

    stockgroup = sf.StockGroup(stock, stock_b)
    stockgroup_nested = sf.StockGroup(stockgroup, sf.Stock("C"))
    flowgroup = sf.FlowGroup(flow, flow_b)
    # Groups
    stockgroup.graphviz
    stockgroup_nested.graphviz

    flowgroup.graphviz