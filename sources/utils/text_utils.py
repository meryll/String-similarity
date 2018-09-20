import distance
import re


def get_distance(seq1, seq2):
    """
    Get distance between two sequences
    :param seq1:
    :param seq2:
    :return:
    """
    seq1 = _prepare(seq1)
    seq2 = _prepare(seq2)

    string_distance = distance.levenshtein(seq1, seq2, normalized=True)
    # string_distance4 = textdistance.jaro_winkler(seq1, seq2)

    return string_distance


# todo this shouldn't be done on every iteration
def _prepare(sequence):
    sequence = re.sub(r'[^\w\s]', '', sequence)
    return sequence.lower()


def clean(sequence, substring):
    return sequence.replace(substring,'').strip()

