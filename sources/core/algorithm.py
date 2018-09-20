import copy
from sources.utils import text_utils, collections_utils, metrics_utils


def _get_best_synonym_for_description(code_desc, unused_synonyms):
    """
    Returning best matching string from collection based on string distance.
    :param code_desc: code description for which we are looking for the best matching synonym
    :param unused_synonyms: all the synonyms we are compering to code_desc
    :return: best matching string and its distance.
    """
    chosen_synonym = ''
    chosen_distance = float('inf')

    for synonym in unused_synonyms:
        string_distance = text_utils.get_distance(code_desc, synonym)

        if string_distance < chosen_distance:
            chosen_synonym = synonym
            chosen_distance = string_distance

    return chosen_synonym, chosen_distance


def _perform_first_iteration(C, unused_synonyms):
    """
    Performing first matching iteration.
    For each new code description in C we are finding closest synonym from T.
    This adds duplicates to the C* (to change it we should delete used synonym after each single iteration)
    :param C: new code descriptions to enrich
    :param unused_synonyms: all unused synonyms that can be used to
    :return: all synonyms that have been match in the first iteration
    """
    all_chosen_synonyms = {}

    for new_code in C.code_ids:
        new_code_desc = C.code_ids[new_code]

        chosen_attractor, chosen_distance = _get_best_synonym_for_description(code_desc=new_code_desc,
                                                                              unused_synonyms=unused_synonyms)
        confidence = metrics_utils.get_confidence(distance=chosen_distance, shared_codes=None)

        all_chosen_synonyms[chosen_attractor] = (new_code, confidence)
        C.add_new_attractor(code=new_code,
                            synonym=chosen_attractor,
                            distance=chosen_distance,
                            shared_codes=None,
                            confidence=confidence)

    collections_utils.reduce_dictionary(to_reduce=unused_synonyms, to_delete=all_chosen_synonyms)
    return all_chosen_synonyms


def _match_all_unused_synonyms(C, T, unused_synonyms, all_chosen_synonyms, confidance_threshold):
    """
    Matching all synonyms from list to 'closest' synonym in another list,
    based on string distance and number of shared codes.
    todo: take into consideration also string distance between new synonym and code description
    :param C: new code descriptions
    :param T:
    :param unused_synonyms:
    :param all_chosen_synonyms: dictionary,  key=synonym, value (new_codeId, confidence)
    :return:
    """
    iterator = 1
    for synonym in unused_synonyms:
        print("Enriching {}/{}".format(iterator, len(unused_synonyms)))
        iterator += 1

        row_for_new_synonym = T.get_row_for_synonym(synonym)

        chosen_shared_codes = 0
        chosen_distance = float('inf')
        chosen_attractor = ''
        chosen_confidence = 0

        for already_chosen in all_chosen_synonyms:
            confidence_for_parent_synonym = all_chosen_synonyms[already_chosen][1]
            row_for_synonym = T.get_row_for_synonym(already_chosen)
            current_shared_codes = metrics_utils.calculate_shared_codes(T.T[row_for_new_synonym], T.T[row_for_synonym])

            current_distance = text_utils.get_distance(synonym, already_chosen)
            current_confidence = metrics_utils.get_confidence(distance=current_distance,
                                                              shared_codes=current_shared_codes,
                                                              parent_confidence=confidence_for_parent_synonym)

            if current_confidence > chosen_confidence:
                chosen_shared_codes = current_shared_codes
                chosen_distance = current_distance
                chosen_attractor = already_chosen
                chosen_confidence = current_confidence

        if _should_add(confidence=chosen_confidence, confidence_threshold=confidance_threshold):
            for_code = all_chosen_synonyms[chosen_attractor][0]
            all_chosen_synonyms[synonym] = (for_code, chosen_confidence)
            C.add_new_attractor(code=for_code,
                                synonym=synonym,
                                distance=chosen_distance,
                                shared_codes=chosen_shared_codes,
                                confidence=chosen_confidence)


def enrich(T, C_original, confidance_threshold):
    print("Code descriptions to enrich {}".format(C_original.get_length()))

    C = copy.deepcopy(C_original)
    unused_synonyms = copy.deepcopy(T.synonym_to_id_lookup_table)

    all_chosen_synonyms = _perform_first_iteration(C=C,
                                                   unused_synonyms=unused_synonyms)

    _match_all_unused_synonyms(C=C, T=T,
                               all_chosen_synonyms=all_chosen_synonyms,
                               unused_synonyms=unused_synonyms,
                               confidance_threshold=confidance_threshold)

    return C


def _should_add(confidence, confidence_threshold):
    return confidence > confidence_threshold
