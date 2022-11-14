from gendiff.formatters.stylish import value_to_str
from gendiff.formatters.plain import plain_value


def test_value_to_str():
    assert value_to_str(True, 0) == 'true'
    assert value_to_str(15, 0) == '15'
    assert value_to_str(None, 0) == 'null'


def test_plain_value(file1):
    assert plain_value(file1) == '[complex value]'
    assert plain_value(True) == 'true'
    assert plain_value(False) == 'false'
    assert plain_value(None) == 'null'
    assert plain_value('Grace') == "'Grace'"
