def calculate_shared_codes(a, b, normalized=True):
    """
    Calculating count of shared numbers in two vectors.
    :param a: vector 1
    :param b: vector 2
    :param normalized: if we should normalize output to <0,1>
    :return: count of the same numbers in two vectors
    """
    non_zero_a = list(filter(lambda x: x != 0, a))
    non_zero_b = list(filter(lambda x: x != 0, b))
    all_shared_codes = len(set(non_zero_a) & set(non_zero_b))
    if normalized:
        return all_shared_codes/len(a)
    return all_shared_codes


def get_confidence(distance, parent_confidence=1.0, shared_codes=None):
    if shared_codes is None:
        current_confidence = 1-distance
    else:
        current_confidence = (shared_codes+(1-distance))/2

    return current_confidence*parent_confidence
