from gendiff.modules.formatters.stylish import stylish_format
from gendiff.modules.formatters.plain import plain_format
from gendiff.modules.formatters.json import json_format


def use_format(diff_result, format):
    if format == 'stylish':
        return stylish_format(diff_result)
    if format == 'plain':
        return plain_format(diff_result)
    if format == 'json':
        return json_format(diff_result)
