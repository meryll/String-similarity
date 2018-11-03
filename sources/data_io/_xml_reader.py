import xml.etree.ElementTree
from sources.utils import random_utils, text_utils


def read(file_path):
    code_suffix = random_utils.suffix_generator()

    root = xml.etree.ElementTree.parse(file_path).getroot()

    core_descriptions = {}
    new_code_to_old = {}
    code_to_synonym = []
    synonym_to_synonym = []

    for code_record in root.iter('CodeRecord'):
        old_code_id = code_record.find('CodeID').text
        code_id = code_suffix+old_code_id
        new_code_to_old[code_id] = old_code_id

        code_desc_dirty = code_record.find('CodeDescription').text
        code_desc = text_utils.clean(sequence=code_desc_dirty, substring=old_code_id)

        core_descriptions[code_id] = code_desc

        for child in code_record.iter('Instance'):
            synonym = child.find('InstanceDescription').text
            code_to_synonym.append(code_id)
            synonym_to_synonym.append(synonym.lower())

    print("Done reading xml")
    return core_descriptions, code_to_synonym,synonym_to_synonym, new_code_to_old
