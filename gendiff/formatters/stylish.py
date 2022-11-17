import itertools


def value_to_str(value, depth, indent='    '):
    if isinstance(value, dict):
        result = []
        for k, v in value.items():
            space = indent * (depth + 1)
            result.append(f"\n{space}{k}: {value_to_str(v, depth + 1)}")
        line = itertools.chain('{', result, '\n', [indent * depth, '}'])
        return ''.join(line)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def build_line(data, key, depth, indent='  '):
    return f"{'  ' * depth}{indent}{data['key']}: " \
           f"{value_to_str(data[key], depth + 1)}"


def stylish_format(diff_result):

    def walk(node, depth=0, replacer='  ', indent='    '):
        lines = []
        space = replacer * (depth + 1)
        for k, v in node.items():
            if v['operation'] == 'nested':
                lines.append(f"{space * 2}{v['key']}: "
                             f"{walk(v['value'], depth + 1)}")
            if v['operation'] == 'unchanged':
                lines.append(f"{space}{build_line(v, 'value', depth)}")
            if v['operation'] == 'changed':
                lines.append(f"{space}{build_line(v, 'old', depth, '- ')}")
                lines.append(f"{space}{build_line(v, 'new', depth, '+ ')}")
            if v['operation'] == 'removed':
                lines.append(f"{space}{build_line(v, 'value', depth, '- ')}")
            if v['operation'] == 'added':
                lines.append(f"{space}{build_line(v, 'value', depth, '+ ')}")
        result = itertools.chain('{', lines, [indent * depth + '}'])
        return "\n".join(result)
    return walk(diff_result)
