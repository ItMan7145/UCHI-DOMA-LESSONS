from unittest import TestCase
from a1 import get_avg_lists


class TestGetAvg(TestCase):
    def test_mixin_nums(self):
        lst1 = [0, 1, 2, 909, 897]
        lst2 = [34254, 1, 23452345, 909, 1]

        result = 455

        self.assertEqual(get_avg_lists(lst1, lst2), result, 'Hi from indus! :)')

    def test_mixin_nums2(self):
        lst1 = []
        lst2 = [6356, 54363, 345634, 346346]

        result = 0

        self.assertEqual(get_avg_lists(lst1, lst2), result)

    def test_mixin_str(self):
        lst1 = ['aboba', 2, 1]
        lst2 = ['aboba', 1, 5]

        result = 1

        self.assertEqual(get_avg_lists(lst1, lst2), result, 'Hi from indus')
