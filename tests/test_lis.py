import unittest
from src.bsqrate.bsqrate import BSQRate


class TestLIS(unittest.TestCase):
    def lis_equal(self, values: list, true_ids: list, msg=None):
        id_key = 'id'
        x_key = 'true_bitrate'
        launches = [{id_key: i, x_key: k} for i, k in enumerate(values)]
        monotonic_launches = BSQRate.filter_monotonic(launches, x_key)
        pred_ids = [i[id_key] for i in monotonic_launches]
        self.assertListEqual(true_ids, pred_ids, msg=msg)

    def test_monotonic(self):
        self.lis_equal([0.0, 0.1, 0.2, 0.3], [0, 1, 2, 3])

    def test_not_monotonic_easy(self):
        self.lis_equal([0.0, 0.1, 0.3, 0.2, 0.4], [0, 1, 2, 4])

    def test_not_monotonic_lis(self):
        self.lis_equal([0.0, 0.1, 0.5, 0.2, 0.3, 0.4], [0, 1, 3, 4, 5])

    def test_equal_first(self):
        self.lis_equal([0.0, 0.1, 0.1, 0.2], [0, 1, 3])

    def test_not_monotonic_first(self):
        self.lis_equal([0.0, 0.3, 0.4, 0.1, 0.2], [0, 1, 2])
