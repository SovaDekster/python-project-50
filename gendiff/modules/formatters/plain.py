from gendiff.modules.dict_settings import modified_value


def plain(diff_result: dict, path: str = None):
    if path is None:
        path = str()
    result = ''
    for k, v in diff_result.items():
        current_path = f"{path}{v['key']}"
        if v['operation'] == 'changed':
            result += f"Property '{current_path}' was updated. From {modified_value(v['old'])} to {modified_value(v['new'])}\n"
        elif v['operation'] == 'removed':
            result += f"Property '{current_path}' was removed\n"
        elif v['operation'] == 'added':
            result += f"Property '{current_path}' was added with value: {modified_value(v['value'])}\n"
        elif v['operation'] == 'nested':
            result += plain(v['value'], current_path + '.') + '\n'
    return result[:-1]


if __name__ == '__main__':
    plain(diff_result)
