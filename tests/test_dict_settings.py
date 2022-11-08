from gendiff.modules.dict_settings import set_bool_and_none_low, \
    set_common_and_difference, new_dict_value, new_dict_key


def test_set_bool_and_none_low_empty_dict():
    assert set_bool_and_none_low({}) == {}


def test_set_bool_and_none_low(file1):
    assert set_bool_and_none_low(file1) == {
        'host': "hexlet.io",
        'timeout': 50,
        'proxy': "123.234.53.22",
        'follow': 'false'
    }


def test_set_bool_and_none_low(file2):
    assert set_bool_and_none_low(file2) == {
        'timeout': 'null',
        'verbose': 'true',
        'host': "hexlet.io"
    }


def test_set_common_and_difference(file1, file2):
    common, removed, added = set_common_and_difference(file1, file2)
    assert common == {'host', 'timeout'}
    assert removed == {'proxy', 'follow'}
    assert added == {'verbose'}


def test_new_dict_value(file1):
    assert new_dict_value(file1) == {
        '  host': "hexlet.io",
        '  timeout': 50,
        '  proxy': "123.234.53.22",
        '  follow': False
    }


def test_new_dict_value_is_not_dict(value='Grace'):
    assert new_dict_value(value='Grace') == 'Grace'


def test_new_dict_key(key='host'):
    assert new_dict_key(key='host') == '  host'
