"""
Container for similar stocks

"""
from collections.abc import Iterable

from systemflow.core import group
from systemflow.core import stock

class StockGroup(group.ContainerMixin):
    _allowed_types = (stock.Stock,)
    _element_name = 'stock'