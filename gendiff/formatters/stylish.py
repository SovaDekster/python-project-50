import itertools


def value_to_str(value, depth, indent='    '):
    if isinstance(value, dict):
        result = []
        for k, v in value.items():
            space = indent * (depth + 1)
            result.append(f"\n{space}{k}: {value_to_str(v, depth + 1)}")
        line = itertools.chain('{', result, '\n', [indent * depth, '}'])
        return ''.join(line)
    else:
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
    return str(value)


def build_line(data, key, depth, indent='  '):
    line = f"{'  ' * depth}{indent}{data['key']}: " \
           f"{value_to_str(data[key], depth + 1)}"
    return line


def stylish_format(diff_result):

    def walk(node, depth=0, replacer='  ', indent='    '):
        strings = []
        space = replacer * (depth + 1)
        for k, v in node.items():
            if v['operation'] == 'nested':
                strings.append(f"\n{space * 2}{v['key']}: {walk(v['value'], depth + 1)}")
            elif v['operation'] == 'unchanged':
                strings.append(f"\n{space}{build_line(v, 'value', depth)}")
            elif v['operation'] == 'changed':
                strings.append(f"\n{space}{build_line(v, 'old', depth, '- ')}")
                strings.append(f"\n{space}{build_line(v, 'new', depth, '+ ')}")
            elif v['operation'] == 'removed':
                strings.append(f"\n{space}{build_line(v, 'value', depth, '- ')}")
            elif v['operation'] == 'added':
                strings.append(f"\n{space}{build_line(v, 'value', depth, '+ ')}")
        result = itertools.chain('{', strings, '\n', [indent * depth + '}'])
        return ''.join(result)
    return walk(diff_result)
