from gendiff.modules.diff import diff


def test_diff(file1_dict, file2_dict, diff_example):
    assert diff(file1_dict, file2_dict) == diff_example


def test_diff_plain(file1_dict_plain, file2_dict_plain, diff_example_plain):
    assert diff(file1_dict_plain, file2_dict_plain) == diff_example_plain
