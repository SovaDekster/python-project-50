from gendiff import generate_diff
from gendiff.modules.generate_diff import stylish


def test_generate_diff_json(path1_json, path2_json):
    with open('tests/fixtures/result_diff.txt', 'r') as result:
        assert generate_diff(path1_json, path2_json) == result.read().rstrip()


def test_generate_diff_yml(path1_yml, path2_yml):
    with open('tests/fixtures/result_diff.txt', 'r') as result:
        assert generate_diff(path1_yml, path2_yml) == result.read().rstrip()


def test_stylish(diff_example):
    with open('tests/fixtures/result_diff.txt', 'r') as result:
        assert stylish(diff_example) == result.read().rstrip()


def test_generate_diff_plain_json(path1_plain_json, path2_plain_json):
    with open('tests/fixtures/result_for_plain_diff.txt', 'r') as result:
        assert generate_diff(path1_plain_json, path2_plain_json) == result.read().rstrip()


def test_generate_diff_plain_yml(path1_plain_yml, path2_plain_yml):
    with open('tests/fixtures/result_for_plain_diff.txt', 'r') as result:
        assert generate_diff(path1_plain_yml, path2_plain_yml) == result.read().rstrip()
