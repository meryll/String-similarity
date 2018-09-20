import unittest
from textkernel.utils import collections_utils


class TestCollectionsUtils(unittest.TestCase):


    def test_get_combined(self):
        list_of_lists = [[2, 3, 5],
                         [29, 3, 6],
                         [2, 3, 1]]

        sum = 0
        for list in list_of_lists:
            sum +=len(list)

        combined = collections_utils.get_combined_list(list_of_lists)
        self.assertEqual(len(combined),sum)


    def test_combine_dicts(self):
        dict1 = {}
        dict1['a'] = 'a'
        dict1['b'] = 'b'

        dict2 = {}
        dict2['c'] = 'c'
        dict2['d'] = 'd'

        list_of_lists = []
        list_of_lists.append(dict1)
        list_of_lists.append(dict2)

        combined = collections_utils.get_combined_dicts(list_of_lists)
        self.assertEqual(len(combined),4)

    def test_dict_recude(self):
        dict = {}
        dict['a'] = 'aa'
        dict['b'] = 'bb'
        dict['c'] = 'cc'

        to_delete = {}
        to_delete['a'] = 'c'
        to_delete['z'] = 'z'
        collections_utils.reduce_dictionary(to_reduce=dict, to_delete=to_delete)
        self.assertEqual(2,len(dict))