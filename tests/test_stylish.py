from gendiff.modules.generate_diff import stylish


def test_stylish(diff_example):
    with open('tests/fixtures/result_for_stylish_diff.txt', 'r') as result:
        assert stylish(diff_example) == result.read()
