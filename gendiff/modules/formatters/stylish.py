import itertools


def stylish_value(value, depth):
    if isinstance(value, dict):
        string = ''
        for k, v in value.items():
            space = '    ' * (depth + 1)
            string += f"\n{space}{k}: {stylish_value(v, depth + 1)}"
        line = itertools.chain('{', string, '\n', ['    ' * depth, '}'])
        return ''.join(line)
    else:
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        else:
            return str(value)


def make_string(dictionary, key, depth, symbol='  '):
    string = f"{'  ' * depth}{symbol}{dictionary['key']}: " \
             f"{stylish_value(dictionary[key], depth + 1)}"
    return string


def stylish_format(diff_result):

    def walk(node, depth, replacer='  '):
        strings = ''
        space = replacer * (depth + 1)
        for k, v in node.items():
            if v['operation'] == 'nested':
                strings += f"\n{space * 2}{v['key']}: {walk(v['value'], depth + 1)}"
            elif v['operation'] == 'unchanged':
                strings += f"\n{space}{make_string(v, 'value', depth)}"
            elif v['operation'] == 'changed':
                strings += f"\n{space}{make_string(v, 'old', depth, '- ')}"
                strings += f"\n{space}{make_string(v, 'new', depth, '+ ')}"
            elif v['operation'] == 'removed':
                strings += f"\n{space}{make_string(v, 'value', depth, '- ')}"
            elif v['operation'] == 'added':
                strings += f"\n{space}{make_string(v, 'value', depth, '+ ')}"
        result = itertools.chain('{', strings, '\n', ['    ' * depth + '}'])
        return ''.join(result)
    return walk(diff_result, 0)
