from gendiff.modules.formatters.json import json_format


def test_json_format(diff_example):
    with open('tests/fixtures/result_for_json_diff.txt', 'r') as result:
        assert json_format(diff_example) == result.read()
