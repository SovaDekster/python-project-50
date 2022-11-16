import json
import pytest
from tests import FIXTURES_PATH
from gendiff.formatters.stylish import value_to_str
from gendiff.formatters.plain import to_str


@pytest.fixture
def file1():
    with open(f"{FIXTURES_PATH}/example_file1.json", 'r') as result:
        return json.load(result)


def test_value_to_str():
    assert value_to_str(True, 0) == 'true'
    assert value_to_str(15, 0) == '15'
    assert value_to_str(None, 0) == 'null'


def test_to_str(file1):
    assert to_str(file1) == '[complex value]'
    assert to_str(True) == 'true'
    assert to_str(False) == 'false'
    assert to_str(None) == 'null'
    assert to_str('Grace') == "'Grace'"
