from gendiff.formatters.stylish import stylish_value
from gendiff.formatters.plain import plain_value
from gendiff.formatters.json import json_value


def test_stylish_value():
    assert stylish_value(True, 0) == 'true'
    assert stylish_value(15, 0) == '15'
    assert stylish_value(None, 0) == 'null'


def test_plain_value(file1):
    assert plain_value(file1) == '[complex value]'
    assert plain_value(True) == 'true'
    assert plain_value(False) == 'false'
    assert plain_value(None) == 'null'
    assert plain_value('Grace') == "'Grace'"


def test_json_value(file1):
    assert json_value(15) == 15
    assert json_value('') is None
    assert json_value(file1) == {
        'host': "hexlet.io",
        'timeout': 50,
        'proxy': "123.234.53.22",
        'follow': False
    }
