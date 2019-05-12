import unittest
import insertionSort
arr = [1, 0, 5, 6, 9, 10, 19, 16]

class TestInsertionSort(unittest.TestCase):
    """ defining a class and inheriting from the unittest"""
    def test_insertionSort(self):
        """defining a function starting with test and the filename of the imported"""
        result = insertionSort.insertionSort(arr)
        self.assertListEqual(result, [0,1,5,6,9,10,16,19])
