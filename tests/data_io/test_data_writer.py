import unittest
from sources.data_io import data_writer


class TestDataWriter(unittest.TestCase):

    def test_get_transfer_type(self):
        threshold = 0.5
        confidences_manual = [0.21,0.3,0.444]

        for confidence in confidences_manual:
            self.assertEqual('manual',data_writer._get_transfer_type(confidence=confidence,threshold=threshold))

        confidences_auto = [0.5, 0.6, 0.99]

        for confidence in confidences_auto:
            self.assertEqual('auto', data_writer._get_transfer_type(confidence=confidence, threshold=threshold))

