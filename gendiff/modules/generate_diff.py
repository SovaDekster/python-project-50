import itertools
from gendiff.modules.parser import open_file
from gendiff.modules.dict_settings import set_bool_to_low
from gendiff.modules.dict_settings import set_common_and_difference


def generate_diff(path1, path2):
    dict1 = open_file(path1)
    dict2 = open_file(path2)
    file1 = set_bool_to_low(dict1)
    file2 = set_bool_to_low(dict2)
    common, diff_file1, diff_file2 = set_common_and_difference(file1, file2)
    sorted_files = sorted(common | diff_file1 | diff_file2)

    diff = ''

    for key in sorted_files:
        if key in common and file1[key] == file2[key]:
            diff += f'\n    {key}: {file1[key]}'
        if key in common and file1[key] != file2[key]:
            diff += f'\n  - {key}: {file1[key]}'
            diff += f'\n  + {key}: {file2[key]}'
        if key in diff_file1:
            diff += f'\n  - {key}: {file1[key]}'
        if key in diff_file2:
            diff += f'\n  + {key}: {file2[key]}'
        result = itertools.chain('{', diff, '\n}')
    return ''.join(result)


if __name__ == '__main__':
    generate_diff(file1, file2)  # noqa F821
