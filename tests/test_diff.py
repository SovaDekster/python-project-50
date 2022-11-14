import pytest
from ast import literal_eval
from gendiff.diff import diff


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
        'timeout': None,
        'verbose': True,
        'host': "hexlet.io"
    }


parameters = [('file1', 'file2', 'tests/fixtures/simple_diff.txt')]


@pytest.mark.parametrize('arg1, arg2, expected', parameters)
def test_diff(arg1, arg2, expected, request):
    arg1_value = request.getfixturevalue(arg1)
    arg2_value = request.getfixturevalue(arg2)
    with open(expected) as result:
        diff_result = literal_eval(result.read())
        assert diff(arg1_value, arg2_value) == diff_result
