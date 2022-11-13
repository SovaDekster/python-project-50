import pytest
from ast import literal_eval
from gendiff.diff import diff, set_common_and_difference


parameters = [('file1', 'file2', 'tests/fixtures/simple_diff.txt'),
              ('file1_dict', 'file2_dict', 'tests/fixtures/diff_file.txt')]


@pytest.mark.parametrize('arg1, arg2, expected', parameters)
def test_diff(arg1, arg2, expected, request):
    arg1_value = request.getfixturevalue(arg1)
    arg2_value = request.getfixturevalue(arg2)
    with open(expected) as result:
        diff_result = literal_eval(result.read())
        assert diff(arg1_value, arg2_value) == diff_result


def test_set_common_and_difference(file1, file2):
    common, removed, added = set_common_and_difference(file1, file2)
    assert common == {'host', 'timeout'}
    assert removed == {'proxy', 'follow'}
    assert added == {'verbose'}
