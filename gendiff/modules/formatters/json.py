import json
from gendiff.modules.dict_settings import json_value


def json_format(diff_result):
    result = json_value(diff_result)
    return json.dumps(result)


if __name__ == '__main__':
    json_format(diff_result)
