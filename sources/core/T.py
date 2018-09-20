from sources.data_io import data_reader
from sources.utils import lookup_table_utils
from sources.utils import collections_utils
import numpy as np


class T:

    def __init__(self, file_paths):
        self._get_raw_data(file_paths=file_paths)
        self._preprocess_data()

    def get_row_for_synonym(self, synonym):
        """
        Synonyms ids start from 1 (beacuse 0 means that synonym was not present in a taxonomy
        but row numbers in matrix start from 1.
        :param synonym:
        :return: row number
        """
        return self.synonym_to_id_lookup_table[synonym] - 1

    def _get_raw_data(self, file_paths):
        self.all_code_ids = []
        self.all_synonyms_parent_codes = []
        self.all_synonyms_values = []

        for file_path in file_paths:
            code_ids, synonym_parent_code, synonym_values, new_code_to_old = data_reader.get(file_path)

            self.all_code_ids.append(code_ids)
            self.all_synonyms_parent_codes.append(synonym_parent_code)
            self.all_synonyms_values.append(synonym_values)

    def _preprocess_data(self):
        """
        Creating T matrix from raw data
        :return:
        """
        self.N = len(self.all_synonyms_parent_codes)

        combined_code_ids_dict = collections_utils.get_combined_dicts(self.all_code_ids)
        combined_synonyms_values = collections_utils.get_combined_list(list_of_lists=self.all_synonyms_values)

        self.codes_to_id_lookup_table = lookup_table_utils.create_id_lookup_table(list=list(combined_code_ids_dict.keys()))
        self.synonym_to_id_lookup_table = lookup_table_utils.create_id_lookup_table(list=set(combined_synonyms_values))

        self.M = len(self.synonym_to_id_lookup_table)
        self.T = np.zeros((self.M, self.N))

        for n in range(self.N):
            for parent_code, synonym_value in zip(self.all_synonyms_parent_codes[n], self.all_synonyms_values[n]):
                parent_code_id = self.codes_to_id_lookup_table[parent_code]
                synonym_row = self.synonym_to_id_lookup_table[synonym_value] - 1
                self.T[synonym_row, n] = parent_code_id
