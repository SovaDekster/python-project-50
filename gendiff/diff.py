def diff(dict1, dict2):
    keys = sorted(dict1.keys() | dict2.keys())
    added = dict2.keys() - dict1.keys()
    removed = dict1.keys() - dict2.keys()
    result = {}
    for k in keys:
        description = {'key': k}
        if k in removed:
            description['operation'] = 'removed'
            description['value'] = dict1[k]
        elif k in added:
            description['operation'] = 'added'
            description['value'] = dict2[k]
        elif dict1[k] == dict2[k]:
            description['operation'] = 'unchanged'
            description['value'] = dict1[k]
        elif all(
            [isinstance(dict1[k], dict),
             isinstance(dict2[k], dict)]
        ):
            description['operation'] = 'nested'
            description['value'] = diff(dict1[k], dict2[k])
        else:
            description['operation'] = 'changed'
            description['old'] = dict1[k]
            description['new'] = dict2[k]
        result[k] = description
    return result
