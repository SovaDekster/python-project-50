from gendiff.modules.dict_settings import set_bool_and_none_low, \
    set_common_and_difference, new_dict_value, new_dict_key


def diff(file1, file2):  # noqa C901
    file1 = set_bool_and_none_low(file1)
    file2 = set_bool_and_none_low(file2)
    common, removed, added = set_common_and_difference(file1, file2)
    dict_sorted = sorted(common | removed | added)
    diff_result = {}
    for key in dict_sorted:
        if key in added:
            file2[key] = new_dict_value(file2[key])
            key_new = new_dict_key(key, '+ ')
            diff_result[key_new] = file2[key]
        elif key in removed:
            file1[key] = new_dict_value(file1[key])
            key_new = new_dict_key(key, '- ')
            diff_result[key_new] = file1[key]
        else:
            if isinstance(file1[key], dict) and isinstance(file2[key], dict):
                key_new = new_dict_key(key)
                diff_result[key_new] = diff(file1[key], file2[key])
            elif any(
                    [isinstance(file1[key], dict),
                     isinstance(file2[key], dict),
                     file1[key] != file2[key]]):
                key_new1 = new_dict_key(key, '- ')
                diff_result[key_new1] = new_dict_value(file1[key])
                key_new2 = new_dict_key(key, '+ ')
                diff_result[key_new2] = new_dict_value(file2[key])
            elif file1[key] == file2[key]:
                key_new = new_dict_key(key)
                diff_result[key_new] = file1[key]
    return diff_result


if __name__ == '__main__':
    diff(file1, file2)  # noqa F821
