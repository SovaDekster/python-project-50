import pytest
import json
from gendiff.modules.low_bool import get_bool_to_low


@pytest.fixture
def file():
    return {'a': 'hexlet', 'b': True, 'c': '234'}


def test_get_bool_to_low(file):
    assert get_bool_to_low(file) == {'a': 'hexlet', 'b': 'true', 'c': '234'}
