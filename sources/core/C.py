from sources.data_io import data_reader
from sources.core.attractor import Attractor


class C:

    def __init__(self, file_path):
        self.code_ids, synonym_parent_code, synonym_values, self.new_code_to_old = data_reader.get(file_path)

        self.new_attractors = {}
        for new_code in self.code_ids:
            self.new_attractors[new_code] = list([])

    def add_new_attractor(self, code, synonym, distance, shared_codes, confidence):
        self.new_attractors[code].append(Attractor(synonym, distance, shared_codes, confidence))

    def get_length(self):
        return len(self.code_ids)
