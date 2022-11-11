from gendiff.modules.diff import diff, set_common_and_difference


def test_diff(file1_dict, file2_dict, diff_example):
    assert diff(file1_dict, file2_dict) == diff_example


def test_simple_diff(file1_dict_simple, file2_dict_simple, diff_simple_example):
    assert diff(file1_dict_simple, file2_dict_simple) == diff_simple_example


def test_set_common_and_difference(file1, file2):
    common, removed, added = set_common_and_difference(file1, file2)
    assert common == {'host', 'timeout'}
    assert removed == {'proxy', 'follow'}
    assert added == {'verbose'}
