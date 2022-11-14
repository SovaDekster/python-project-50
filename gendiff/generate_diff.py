from gendiff.parse import get_content_and_extension, parse
from gendiff.diff import diff
from gendiff.formatters.use_formatter import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1, format1 = get_content_and_extension(path1)
    data2, format2 = get_content_and_extension(path2)
    dict1 = parse(data1, format1)
    dict2 = parse(data2, format2)
    result = diff(dict1, dict2)
    return apply_format(result, format)
