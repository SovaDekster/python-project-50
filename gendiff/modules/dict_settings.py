def value_to_string(value):
    if not isinstance(value, dict):
        if value is None:
            value = 'null'
            return value
        if isinstance(value, bool):
            value = str(value).lower()
            return value
        else:
            return value
    for k, v in value.items():
        v = value_to_string(v)
        value[k] = v
    return value


def set_common_and_difference(file1, file2):
    common = file1.keys() & file2.keys()
    removed = file1.keys() - file2.keys()
    added = file2.keys() - file1.keys()
    return common, removed, added


def json_value(value):
    if not isinstance(value, dict):
        if value == 'false':
            return False
        elif value == 'true':
            return True
        elif value == '' or value == 'null':
            return None
        else:
            return value
    for k, v in value.items():
        v = json_value(v)
        value[k] = v
    return value


def modified_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif any(
        [value == 'null',
         value == 'true',
         value == 'false']
    ):
        return value
    return f"'{value}'"


if __name__ == '__main__':
    set_common_and_difference(file1, file2)
    value_to_string(value)
    json_value(value)
    modified_value(value)
