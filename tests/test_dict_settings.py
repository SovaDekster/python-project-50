from gendiff.modules.dict_settings import set_bool_to_low, set_common_and_difference
import pytest


@pytest.fixture
def file1():
    return {'a': 'hexlet', 'b': 'true', 'c': '234'}


@pytest.fixture
def file2():
    return {'a': 'hexlet', 'b': 'false', 'd': 33}


def test_set_bool_to_low(file1):
    assert set_bool_to_low(file1) == {'a': 'hexlet', 'b': 'true', 'c': '234'}


def test_set_bool_to_low_for_empty_dict():
    assert set_bool_to_low({}) == {}


def test_set_common_and_difference(file1, file2):
    common, diff_file1, diff_file2 = set_common_and_difference(file1, file2)
    assert common == {'a', 'b'}
    assert diff_file1 == {'c'}
    assert diff_file2 == {'d'}
