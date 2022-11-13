import pytest
"""This pytest.fixtures are different from fixtures files"""
"""They were created specially for tests"""


@pytest.fixture
def file1():
    return {
        'host': "hexlet.io",
        'timeout': 50,
        'proxy': "123.234.53.22",
        'follow': False
    }


@pytest.fixture
def file2():
    return {
        'timeout': None,
        'verbose': True,
        'host': "hexlet.io"
    }


@pytest.fixture
def file1_dict():
    return {
        "common": {"setting1": "Value 1", "setting2": 200, "setting3": True,
                   "setting6": {"key": "value", "doge": {"wow": ""}}},
        "group1": {"baz": "bas", "foo": "bar", "nest": {"key": "value"}},
        "group2": {"abc": 12345, "deep": {"id": 45}}
    }


@pytest.fixture
def file2_dict():
    return {
        "common": {"follow": False, "setting1": "Value 1", "setting3": None,
                   "setting4": "blah blah", "setting5": {"key5": "value5"},
                   "setting6": {"key": "value", "ops": "vops", "doge": {"wow": "so much"}}},
        "group1": {"foo": "bar", "baz": "bars", "nest": "str"},
        "group3": {"deep": {"id": {"number": 45}}, "fee": 100500}
    }
