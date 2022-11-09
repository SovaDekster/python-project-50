from gendiff.modules.formatters.plain import plain
from gendiff.modules.formatters.stylish import stylish
from gendiff.modules.parser import open_file
from gendiff.modules.diff import diff


def generate_diff(path1, path2, formater='stylish'):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    diff_result = diff(dict1, dict2)
    if formater == 'plain':
        return plain(diff_result)
    elif formater == 'stylish':
        return stylish(diff_result)


if __name__ == '__main__':
    generate_diff(path1, path2, formater)
