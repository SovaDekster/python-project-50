from gendiff.modules.dict_settings import set_bool_to_low
from gendiff.modules.dict_settings import set_common_and_difference
import pytest


@pytest.fixture
def file1():
    return {
        'host': "hexlet.io",
        'timeout': 50,
        'proxy': "123.234.53.22",
        'follow': False
    }


@pytest.fixture
def file2():
    return {
        'timeout': 20,
        'verbose': True,
        'host': "hexlet.io"
    }


def test_set_bool_to_low(file1):
    assert set_bool_to_low(file1) == {
        'host': "hexlet.io",
        'timeout': 50,
        'proxy': "123.234.53.22",
        'follow': 'false'
    }


def test_set_bool_to_low_for_empty_dict():
    assert set_bool_to_low({}) == {}


def test_set_common_and_difference(file1, file2):
    common, diff_file1, diff_file2 = set_common_and_difference(file1, file2)
    assert common == {'host', 'timeout'}
    assert diff_file1 == {'proxy', 'follow'}
    assert diff_file2 == {'verbose'}
