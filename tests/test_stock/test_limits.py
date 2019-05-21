import pytest

import systemflow as sf

def test_wrong_initiation_lower_limit():
    with pytest.raises(Exception) as e_info:
        stock = sf.Stock("test", initial_value=-2, lower_limit=0, upper_limit=10)

def test_wrong_initiation_upper_limit():
    with pytest.raises(Exception) as e_info:
        stock = sf.Stock("test", initial_value=11, lower_limit=0, upper_limit=10)

