def set_bool_and_none_low(file):
    for key, value in file.items():
        if isinstance(value, bool):
            value = str(value).lower()
            file[key] = value
        if value is None:
            value = 'null'
            file[key] = value
    return file


def set_common_and_difference(file1, file2):
    common = file1.keys() & file2.keys()
    removed = file1.keys() - file2.keys()
    added = file2.keys() - file1.keys()
    return common, removed, added


def new_dict_value(value, replacer='  '):
    if isinstance(value, dict):
        value = {f'{replacer}{k}': new_dict_value(v) for k, v in value.items()}
    return value


def new_dict_key(key, replacer='  '):
    new_key = f'{replacer}{key}'
    return new_key


if __name__ == '__main__':
    set_bool_and_none_low(file)  # noqa F821
    set_common_and_difference(file1, file2)  # noqa F821
    new_dict_key(key, replacer='  ')  # noqa F821
    new_dict_value(value, replacer='  ')  # noqa F821