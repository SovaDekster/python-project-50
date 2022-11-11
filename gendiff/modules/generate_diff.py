from gendiff.modules.parse import open_file, parse
from gendiff.modules.diff import diff
from gendiff.modules.formatters.use_formatter import use_format


def generate_diff(path1, path2, format='stylish'):
    data1, format1 = open_file(path1)
    data2, format2 = open_file(path2)
    dict1 = parse(data1, format1)
    dict2 = parse(data2, format2)
    result = diff(dict1, dict2)
    return use_format(result, format)
