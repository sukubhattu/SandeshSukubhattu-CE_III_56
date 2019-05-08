import unittest
import mergeSort
arr = [1, 0, 5, 6, 9, 10, 19, 16]
class TestMergeSort(unittest.TestCase):
    def test_mergeSort(self):
        result = mergeSort.mergeSort(arr)
        self.assertListEqual(result, [0,1,5,6,9,10,16,19])
