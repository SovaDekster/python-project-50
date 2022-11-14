import itertools


def value_to_str(value, depth):
    if isinstance(value, dict):
        string = ''
        for k, v in value.items():
            space = '    ' * (depth + 1)
            string += f"\n{space}{k}: {value_to_str(v, depth + 1)}"
        line = itertools.chain('{', string, '\n', ['    ' * depth, '}'])
        return ''.join(line)
    else:
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
    return str(value)


def build_line(dictionary, key, depth, symbol='  '):
    string = f"{'  ' * depth}{symbol}{dictionary['key']}: " \
             f"{value_to_str(dictionary[key], depth + 1)}"
    return string


def stylish_format(diff_result):

    def walk(node, depth=0, replacer='  '):
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
        result = itertools.chain('{', strings, '\n', ['    ' * depth + '}'])
        return ''.join(result)
    return walk(diff_result)
