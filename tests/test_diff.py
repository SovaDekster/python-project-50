import pytest
import json
from gendiff.diff import diff
from tests import FIXTURES_PATH


@pytest.mark.parametrize("file1, file2, expected_path", [
    (
        f"{FIXTURES_PATH}/example_file1.json",
        f"{FIXTURES_PATH}/example_file2.json",
        f"{FIXTURES_PATH}/simple_diff.txt",
    ),
])
def test_diff(file1, file2, expected_path):
    with open(expected_path, "r") as result, \
         open(file1, "r") as open_f1, open(file2, "r") as open_f2:
        diff_result = json.load(result)
        assert diff(json.load(open_f1), json.load(open_f2)) == diff_result
