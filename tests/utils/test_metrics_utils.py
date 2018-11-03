import unittest
from sources.utils import metrics_utils


class TestDataProvider(unittest.TestCase):

    def test_calculate_shared_codes(self):
        vector = [1, 0, 5, 0]
        matrix = [[0, 1, 0, 4],
                  [5, 2, 0, 1],
                  [5, 0, 0, 1],
                  [1, 0, 5, 0],
                  [1, 1, 0, 0],
                  [0, 0, 0, 0]]

        expected_results = [1, 2, 2, 2, 1, 0]
        expected_results_normalized = [0.25, 0.5, 0.5, 0.5, 0.25, 0]

        for i in range(len(expected_results)):
            distance = metrics_utils.calculate_shared_codes(matrix[i], vector, normalized=False)
            distance_norm = metrics_utils.calculate_shared_codes(matrix[i], vector, normalized=True)
            self.assertEqual(distance,expected_results[i])
            self.assertEqual(distance_norm, expected_results_normalized[i])

    def test_get_confidence(self):
        distances = [1.0, 0.5, 0.0, 0.0]
        shared_codes = [None, 0.5, 1.0, None]
        results = [0.0, 0.5, 1.0, 1.0]

        for i in range(len(results)):
            result = metrics_utils.get_confidence(distance=distances[i], shared_codes=shared_codes[i])
            self.assertEqual(result, results[i])


    def test_get_confidence_with_parent(self):
        distances = [1.0, 0.5, 0.0, 0.0]
        shared_codes = [None, 0.5, 1.0, None]
        results = [0.0, 0.25, 0.5, 0.5]

        for i in range(len(results)):
            result = metrics_utils.get_confidence(distance=distances[i], shared_codes=shared_codes[i], parent_confidence=0.5)
            self.assertEqual(result, results[i])
