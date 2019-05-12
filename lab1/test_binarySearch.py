import unittest
import binarySearch
arr = [1,2,3,4,5,6,7,8]
class TestBinarySearch(unittest.TestCase):
    def test_binarySearch(self):
        result1 = binarySearch.BinarySearch(arr,0,len(arr)-1,8)
        self.assertEqual(result1,7)
        result2 = binarySearch.BinarySearch(arr,0,len(arr)-1,9)
        self.assertEqual(result2,-1)
