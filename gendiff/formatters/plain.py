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


def walk(node, path=''):
    result = []
    for k, v in node.items():
        current_path = f"{path}{v['key']}"
        start_line = f"Property '{current_path}'"
        if v['operation'] == 'changed':
            result.append(f"{start_line} was updated. "
                          f"From {to_str(v['old'])} to {to_str(v['new'])}")
        if v['operation'] == 'nested':
            result.append(walk(v['value'], current_path + '.'))
        if v['operation'] == 'removed':
            result.append(f"{start_line} was removed")
        if v['operation'] == 'added':
            result.append(f"{start_line} was added "
                          f"with value: {to_str(v['value'])}")
    return '\n'.join(result)


def plain_format(diff_result: dict):
    return walk(diff_result)
