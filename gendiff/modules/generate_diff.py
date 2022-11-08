import itertools
from gendiff.modules.parser import open_file
from gendiff.modules.diff import diff


def stylish(few_diffs, replacer=' ', spaces_count=2):
    def walk(value, depth):
        if not isinstance(value, dict):
            return str(value)
        lines = ''
        for k, v in value.items():
            space = replacer * spaces_count * (depth + 1)
            if not isinstance(v, dict):
                lines += f'\n{space}{str(k)}: {str(v)}'
            if isinstance(v, dict):
                lines += f'\n{space}{str(k)}: {walk(v, depth+2)}'
        result = itertools.chain(
            '{', lines, '\n', [replacer * spaces_count * depth + '}']
        )
        return ''.join(result)
    return walk(few_diffs, 0)


def generate_diff(path1, path2, formater=stylish):
    file1 = open_file(path1)
    file2 = open_file(path2)
    diff_result = diff(file1, file2)
    return formater(diff_result)


if __name__ == '__main__':
    generate_diff(file1, file2)  # noqa F821
