import pytest

#local
from utils import find_value_in_nested_dict
from utils import filter_by_value


@pytest.mark.filter_by_value
def test_filter_by_value():
    list_of_dicts = [{1: 2}, {2: 3}]
    out = filter_by_value(list_of_dicts=list_of_dicts, filter_value=2)
    assert out == [{1: 2}]


@pytest.mark.find_value_in_nested_dict
def test_find_value_in_nested_dict():
    j = [1, 2, 3]

    f = {1: {2: {3: 4}}}

    assert find_value_in_nested_dict(j, f) == 4
