
def reduce_dictionary(to_reduce, to_delete):
    """
    Remove one dictionary from another based on matching keys
    :param to_reduce:
    :param to_delete:
    :return: modifying to_reduce dic
    """
    for key in to_delete:
        if key in to_reduce:
            del to_reduce[key]


def get_combined_list(list_of_lists):
    """
    Creating 1d list from list of lists
    :param list_of_lists:
    :return: 1d list
    """
    return list(sum(list_of_lists, []))


def get_combined_dicts(list_of_dicts):
    """
    Creating one dictionary from list of dictionaries.
    :param list_of_dicts:
    :return: One dictionary with combined key-values
    """
    if len(list_of_dicts) == 0:
        raise Exception("List of dictionaries is empty")

    combined = list_of_dicts[0]
    for i in range(1, len(list_of_dicts)):
        combined.update(list_of_dicts[i])

    return combined
