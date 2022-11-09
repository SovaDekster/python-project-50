from gendiff.modules.dict_settings import set_common_and_difference, \
    value_to_string


def diff(dictionary1, dictionary2):
    dict1 = value_to_string(dictionary1)
    dict2 = value_to_string(dictionary2)
    common, removed, added = set_common_and_difference(dict1, dict2)
    keys = sorted(common | removed | added)
    result = {}
    for key in keys:
        if key in common and dict1[key] != dict2[key]:
            if (isinstance(dict1[key], dict) and isinstance(dict2[key], dict)):
                description = {
                    'key': key,
                    'operation': 'nested',
                    'value': diff(dict1[key], dict2[key])}
                result[key] = description
            else:
                description = {
                    'key': key,
                    'operation': 'changed',
                    'old': dict1[key],
                    'new': dict2[key]}
                result[key] = description
        elif key in common and dict1[key] == dict2[key]:
            description = {
                'key': key,
                'operation': 'unchanged',
                'value': dict1[key]}
            result[key] = description
        if key in added:
            description = {
                'key': key,
                'operation': 'added',
                'value': dict2[key]}
            result[key] = description
        if key in removed:
            description = {
                'key': key,
                'operation': 'removed',
                'value': dict1[key]}
            result[key] = description
    return result


if __name__ == '__main__':
    diff(dictionary1, dictionary2)
