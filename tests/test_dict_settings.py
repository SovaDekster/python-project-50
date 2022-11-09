from gendiff.modules.dict_settings import value_to_string, \
    set_common_and_difference, modified_value


def test_value_to_string(file1):
    assert value_to_string(None) == 'null'
    assert value_to_string(True) == 'true'
    assert value_to_string(15) == '15'
    assert value_to_string(file1) == {
        'host': "hexlet.io",
        'timeout': '50',
        'proxy': "123.234.53.22",
        'follow': 'false'
    }


def test_set_common_and_difference(file1, file2):
    common, removed, added = set_common_and_difference(file1, file2)
    assert common == {'host', 'timeout'}
    assert removed == {'proxy', 'follow'}
    assert added == {'verbose'}


def test_modified_value(file1):
    assert modified_value(file1) == '[complex value]'


def test_modified_value_another():
    assert modified_value('true') == 'true'
    assert modified_value('false') == 'false'
    assert modified_value('null') == 'null'
    assert modified_value('Grace') == "'Grace'"
