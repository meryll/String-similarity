import unittest
from textkernel.data_io import data_reader


class TestDataReader(unittest.TestCase):

    def test_get_extension(self):
        paths = ['./../data/all.jobtitle_enriched.xml',
                 'all.jobtitle_enriched.xml',
                 '../../data/experience.normalized4',
                 'experience.normalized4',
                 'None']
        extensions = ['.xml', '.xml', '.normalized4', '.normalized4', '']

        for path, extension in zip(paths, extensions):
            returned_extension = data_reader._get_extension(path)
            self.assertEqual(extension, returned_extension)

