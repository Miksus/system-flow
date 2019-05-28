import pytest
import systemflow as sf


def get_stocks(n, initial_value=1):
    return [
        sf.Stock(f"Stock {i}", 
                initial_value=initial_value if isinstance(initial_value, (float, int)) else initial_value[i])
        for i in range(n)
    ]

def test_construct():
    a, b, c, d = get_stocks(4, initial_value=1)
    group = sf.StockGroup(
        a, b, c, d,
        name="test"
    )
    expected = {
        "name": "test",
        "len": 4
    }
    actual = {
        "name": group.name,
        "len": len(group)
    }
    assert expected == actual

    assert isinstance(group["Stock 0"], sf.Stock)
    assert isinstance(group["Stock 1"], sf.Stock)
    assert isinstance(group["Stock 2"], sf.Stock)
    assert isinstance(group["Stock 3"], sf.Stock)


def test_stock_nesting():

    a, b, c, d, e, f, g, h, i, j = get_stocks(10, initial_value=1)
    group = sf.StockGroup(
        a, b, c, sf.StockGroup(
            d, e, sf.StockGroup(
                sf.StockGroup(
                    f, g, name="sub sub sub test"
                ), h, i, j, name="sub sub test"
            ),
            name="sub test"
        ), name="main test"
    )
    for stock, elem in zip((a, b, c, d, e, f, g, h, i, j), group.flatten()):
        assert stock == elem