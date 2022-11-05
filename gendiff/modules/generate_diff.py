import json
import itertools
from gendiff.modules.low_bool import get_bool_to_low


def set_common_and_difference(file1, file2):
    common = file1.keys() & file2.keys()
    diff_file1 = file1.keys() - file2.keys()
    diff_file2 = file2.keys() - file1.keys()
    return common, diff_file1, diff_file2


def generate_diff(file1, file2):
    file1 = json.load(open(file1))
    file2 = json.load(open(file2))
    file1 = get_bool_to_low(file1)
    file2 = get_bool_to_low(file2)
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
    generate_diff(file1, file2)
