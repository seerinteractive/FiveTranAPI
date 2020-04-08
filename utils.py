def find_value_in_nested_dict(path, _dict):
    """Finds a value in a dict given the file path in a list
    Args:
        path (list): path of the value
        _dict (dict): dict to traverse

    Returns:
        str: the value in the dict

    Typical usage example:
        j = [1, 2, 3]
        f = {1: {2: {3: 4}}}
        find_value_in_nested_dict(j, f)
        4
    """
    if path:
        i, *_ = path
        _dict = _dict[i]
        path.pop(0)
        return find_value_in_nested_dict(path, _dict)
    else:
        return _dict


def filter_by_value(list_of_dicts, filter_value):
    """Filters a list of dictionaries by a single value
    Args:
        list_of_dicts (list): series of single layer dicts
        filter_value (str): a single value to be filtered

    Returns:
        list(dict): a list of filtered dicts

    Typical usage example:
        list_of_dicts = [{1: 2}, {2: 3}]
        FiveTranAPI.filter_by_value(list_of_dicts=list_of_dicts, filter_value=2)
        [{1: 2}]
    """

    return [_dict for _dict in list_of_dicts if filter_value in _dict.values()]


def filter_by_key(list_of_dicts, filter_key):
    """Filters a list of dictionaries by a single key
    Args:
        list_of_dicts (list): series of single layer dicts
        filter_value (str): a single key to be filtered

    Returns:
        list(dict): a list of filtered dicts
    
    Typical usage example:
        list_of_dicts = [{1: 2}, {2: 3}]
        FiveTranAPI.filter_by_key(list_of_dicts=list_of_dicts, filter_value=2)
        [{2: 3}]
    """

    return [_dict for _dict in list_of_dicts if filter_key in _dict.keys()]
