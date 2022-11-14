import pytest
import json
from ast import literal_eval
from gendiff.diff import diff
from tests import FIXTURES_PATH


@pytest.fixture
def file1():
    with open(f"{FIXTURES_PATH}/example_file1.json", 'r') as result:
        return json.load(result)


@pytest.fixture
def file2():
    with open(f"{FIXTURES_PATH}/example_file2.json", 'r') as result:
        return json.load(result)


def test_diff(file1, file2):
    with open(f"{FIXTURES_PATH}/simple_diff.txt", 'r') as result:
        diff_result = literal_eval(result.read())
        assert diff(file1, file2) == diff_result
