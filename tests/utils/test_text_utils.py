import unittest
from textkernel.utils import text_utils


class TestDataProvider(unittest.TestCase):

    def test_prepare(self):

        dirty = ['Foo', 'Foo,', '^Foo$%', 'foo-Foo']
        cleaned = ['foo','foo','foo','foofoo']

        for i in range(len(dirty)):
            clean = text_utils._prepare(dirty[i])
            self.assertEqual(clean, cleaned[i])

    def test_clean(self):

        dirty = ['123   foo', ' AGF foo  ', 'AGF-123   foo foo']
        substrings = ['123','AGF', 'AGF-123']
        cleaned = ['foo','foo','foo foo']

        for i in range(len(dirty)):
            clean = text_utils.clean(sequence=dirty[i], substring=substrings[i])
            self.assertEqual(clean, cleaned[i])



