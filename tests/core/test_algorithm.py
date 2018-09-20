import unittest
from textkernel.core import algorithm


class TestAlgorithm(unittest.TestCase):

    def test_get_best_synonym_for_description(self):

        code_desc = 'Inzynier'
        to_matched = 'Inzynierka'
        unused = {}
        unused['bla'] = 'a'
        unused[to_matched] = 'b'
        unused['foo'] = 'c'

        synonym, distance = algorithm._get_best_synonym_for_description(unused_synonyms=unused,
                                                                        code_desc=code_desc)
        self.assertEqual(synonym, to_matched)

