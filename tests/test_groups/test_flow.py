
import pytest
import systemflow as sf


def get_stocks(n, initial_value=1):
    return [
        sf.Stock(f"Stock {i}", 
                initial_value=initial_value if isinstance(initial_value, (float, int)) else initial_value[i])
        for i in range(n)
    ]


def test_construct():
    a, b, c, d = get_stocks(4)
    group = sf.FlowGroup(
        b >> a,
        c >> a,
        d >> a,
        name="test"
    )
    expected = {
        "name": "test",
        "len": 3
    }
    actual = {
        "name": group.name,
        "len": len(group)
    }
    assert expected == actual

    assert isinstance(group[0], sf.Flow)
    assert isinstance(group[1], sf.Flow)
    assert isinstance(group[2], sf.Flow)

def test_valve():
    a, b, c, d = get_stocks(4)
    group = sf.FlowGroup(
        b >> a,
        c >> a,
        d >> a,
        name="test"
    )
    group.valve = 5
    assert group[0].valve == 5
    assert group[1].valve == 5
    assert group[2].valve == 5

    computator = sf.computators.ComputatorBase()
    group.valve = computator
    assert group[0].valve is computator
    assert group[1].valve is computator
    assert group[2].valve is computator

def test_run():
    a, b, c, d = get_stocks(4, initial_value=5)
    group = sf.FlowGroup(
        b >> a,
        c >> a,
        d >> a,
        name="test"
    )
    group.valve = 2.5
    group()
    assert a.value == 5 + 2.5 * 3
    assert b.value == 5 - 2.5
    assert c.value == 5 - 2.5
    assert d.value == 5 - 2.5



