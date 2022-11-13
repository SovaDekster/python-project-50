from gendiff import generate_diff
import pytest

parameter = [('path1_plain_json', 'path2_plain_json', 'stylish', 'tests/fixtures/result_for_example_files.txt'),
             ('path1_plain_yml', 'path2_plain_yml', 'stylish', 'tests/fixtures/result_for_example_files.txt'),
             ('path1_json', 'path2_json', 'stylish', 'tests/fixtures/result_for_stylish_diff.txt'),
             ('path1_json', 'path2_json', 'plain', 'tests/fixtures/result_for_plain_diff.txt'),
             ('path1_json', 'path2_json', 'json', 'tests/fixtures/result_for_json_diff.txt'),
             ('path1_yml', 'path2_yml', 'stylish', 'tests/fixtures/result_for_stylish_diff.txt'),
             ('path1_yml', 'path2_yml', 'plain', 'tests/fixtures/result_for_plain_diff.txt'),
             ('path1_yml', 'path2_yml', 'json', 'tests/fixtures/result_for_json_diff.txt')]


@pytest.mark.parametrize("path1, path2, format, expected", parameter)
def test_generate_diff(path1, path2, format, expected, request):
    path1 = request.getfixturevalue(path1)
    path2 = request.getfixturevalue(path2)
    with open(expected) as result:
        assert generate_diff(path1, path2, format) == result.read()
