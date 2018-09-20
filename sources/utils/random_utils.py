import string
import random


def suffix_generator(size=4, chars=string.ascii_uppercase + string.digits):
    """
    Generate random code suffix to maintain unique code id across different taxonomies
    :param size:
    :param chars:
    :return:
    """
    return ''.join(random.choice(chars) for _ in range(size))
