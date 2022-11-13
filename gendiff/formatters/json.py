import json


def json_value(value):  # Убрать не получается, из-за '' всё ломается
    if not isinstance(value, dict):
        if value == '':
            return None
        else:
            return value
    for k, v in value.items():
        v = json_value(v)
        value[k] = v
    return value


def json_format(diff_result):
    result = json_value(diff_result)
    return json.dumps(result)
