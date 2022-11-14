from gendiff.formatters.json import json_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.stylish import stylish_format, build_line
import pytest
from ast import literal_eval


@pytest.fixture
def diff_example():
    with open('tests/fixtures/diff_file.txt', 'r') as result:
        diff_result = literal_eval(result.read())
        return diff_result


def test_json_format(diff_example):
    with open('tests/fixtures/result_for_json_diff.txt', 'r') as result:
        assert json_format(diff_example) == result.read()


def test_plain_format(diff_example):
    with open('tests/fixtures/result_for_plain_diff.txt', 'r') as result:
        assert plain_format(diff_example) == result.read()


def test_stylish_format(diff_example):
    with open('tests/fixtures/result_for_stylish_diff.txt', 'r') as result:
        assert stylish_format(diff_example) == result.read()


def test_build_line():
    assert build_line({'key': 'verbose', 'any': 1}, 'key', 1) == '    verbose: verbose'
