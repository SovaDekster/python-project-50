from gendiff.diff import diff
from gendiff.parser import get_content
from gendiff.formatters.use_formatter import apply_format


def generate_diff(path1, path2, format='stylish'):
    content1 = get_content(path1)
    content2 = get_content(path2)
    result = diff(content1, content2)
    return apply_format(result, format)
