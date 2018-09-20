from sources.utils import random_utils, text_utils


def _is_core_description(string):
    return not string[0] == '-'


def _parse_core_description(dirty_string):
    dirty_string = dirty_string.replace('\n', '')
    parts = dirty_string.split('\t')

    if len(parts) > 1:
        return parts[-2], parts[-1]
    else:
        return None, parts[-1]


def read(file_path):
    code_suffix = random_utils.suffix_generator()
    file = open(file_path, "r")

    core_descriptions = {}
    new_code_to_old = {}
    code_to_synonym = []
    synonym_to_synonym = []

    code_id = ''

    for line in file:
        if _is_core_description(line):
            old_code, code_desc_dirty = _parse_core_description(line)
            code_id = code_suffix + str(old_code)
            new_code_to_old[code_id] = old_code
            code_desc = text_utils.clean(sequence=code_desc_dirty, substring=old_code)
            core_descriptions[code_id] = code_desc
        else:
            synonym = _parse_core_description(line)[1]
            code_to_synonym.append(code_id)
            synonym_to_synonym.append(synonym)

    print("Done reading normalized4")
    return core_descriptions, code_to_synonym, synonym_to_synonym, new_code_to_old
