def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, int):
        return value
    return f"'{value}'"


def plain_format(diff_result: dict):

    def walk(node, path=''):
        result = ''
        for k, v in node.items():
            current_path = f"{path}{v['key']}"
            if v['operation'] == 'changed':
                result += f"Property '{current_path}' was updated. From {to_str(v['old'])} to {to_str(v['new'])}\n"
            elif v['operation'] == 'nested':
                result += walk(v['value'], current_path + '.') + '\n'
            elif v['operation'] == 'removed':
                result += f"Property '{current_path}' was removed\n"
            elif v['operation'] == 'added':
                result += f"Property '{current_path}' was added with value: {to_str(v['value'])}\n"
        return result[:-1]
    return walk(diff_result)
