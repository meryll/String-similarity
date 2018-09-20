import unittest
from textkernel.data_io import _normalized_file_reader

class TestNormalizedFileReader(unittest.TestCase):

    def test_is_core_desription(self):
        descriptions = ['177\tAdministrator\n','12-AAA\t12345\n','177-\tA\n','0\tAkr\n','1\tSolicitor Non-Commercial\n']
        not_decriptions = ['-\t- office administrator\n', '-\t sales administrator\n', '-\tdministration manager\n', '-\tFundraiser\n', '-\tHotel Manager\n', '-\tOther IT\n', '-\tit technician\n', '-\tnetwork support analyst\n']

        for desc in descriptions:
            result = _normalized_file_reader._is_core_description(desc)
            self.assertEqual(True, result)

        for desc in not_decriptions:
            result = _normalized_file_reader._is_core_description(desc)
            self.assertEqual(False, result)

    def test_parse_core_description(self):
        dirty_descriptions = ['177\tAdministrator Two\n', '12-AAA\t12345\n', '177-\tA-A\n', '0\tAkr_A\n', '1\tAd\n','Nic']
        clean_descriptions = ['Administrator Two','12345','A-A','Akr_A','Ad', 'Nic']
        clean_ids = ['177', '12-AAA', '177-', '0', '1', None]

        for i in range(len(dirty_descriptions)):
            clean_code, clean_desc = _normalized_file_reader._parse_core_description(dirty_descriptions[i])
            self.assertEqual(clean_code, clean_ids[i])
            self.assertEqual(clean_desc, clean_descriptions[i])
