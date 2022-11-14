import pytest
from ast import literal_eval
from tests import FIXTURES_PATH
from gendiff.formatters.stylish import build_line
from gendiff.formatters.use_formatter import apply_format


@pytest.mark.parametrize("file, expected_path, format", [
    (
        f"{FIXTURES_PATH}/diff_file.txt",
        f"{FIXTURES_PATH}/result_for_json_diff.txt",
        'json'
    ),
    (
        f"{FIXTURES_PATH}/diff_file.txt",
        f"{FIXTURES_PATH}/result_for_plain_diff.txt",
        'plain'
    ),
    (
        f"{FIXTURES_PATH}/diff_file.txt",
        f"{FIXTURES_PATH}/result_for_stylish_diff.txt",
        'stylish'
    ),
])
def test_apply_format(file, expected_path, format):
    with open(expected_path, "r") as result:
        open_file = open(file, "r")
        diff_file = literal_eval(open_file.read())
        apply_format(diff_file, format) == result.read()


def test_build_line():
    assert build_line({'key': 'verbose', 'any': 1}, 'key', 1) == '    verbose: verbose'
