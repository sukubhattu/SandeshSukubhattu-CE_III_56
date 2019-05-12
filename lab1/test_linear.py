import unittest
import linear

arr = [1, 0, 5, 6, 9, 10, 19, 16]
class TestLinear(unittest.TestCase):

    def test_LinearSearch(self):
        result = linear.LinearSearch(arr, 15)
        self.assertEqual(result,-1)
