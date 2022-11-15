from gendiff.diff import diff
from gendiff.parse import get_content_and_extension
from gendiff.formatters.use_formatter import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1 = get_content_and_extension(path1)
    data2 = get_content_and_extension(path2)
    result = diff(data1, data2)
    return apply_format(result, format)
