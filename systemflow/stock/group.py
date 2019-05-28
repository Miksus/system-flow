"""
Container for similar stocks

"""
from collections.abc import Iterable
from systemflow.base import StockBase, ContainerMixin

class StockGroup(StockBase, ContainerMixin):
    _allowed_types = (StockBase,)
    _element_name = 'stock'