import json
import pytest
from gendiff import generate_diff
from gendiff.modules.generate_diff import set_common_and_difference


@pytest.fixture
def file1():
    return {'a': 'hexlet', 'b': 'true', 'c': '234'}


@pytest.fixture
def file2():
    return {'a': 'hexlet', 'b': 'false', 'd': 33}


@pytest.fixture
def f1():
    return 'tests/fixtures/example_file1.json'


@pytest.fixture
def f2():
    return 'tests/fixtures/example_file2.json'


def test_set_common_and_difference(file1, file2):
    common, diff_file1, diff_file2 = set_common_and_difference(file1, file2)
    assert common == {'a', 'b'}
    assert diff_file1 == {'c'}
    assert diff_file2 == {'d'}


def test_generate_diff(f1, f2):
    with open('tests/fixtures/result_json.txt', 'r') as result:
        assert generate_diff(f1, f2) != result.read()
