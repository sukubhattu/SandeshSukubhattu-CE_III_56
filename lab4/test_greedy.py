import unittest
import greedy
s = [1,3,0,5,3,5,6,8,8,2,12]
f = [4,5,6,7,9,9,10,11,12,14,16]
correct=[0,3,7,10]

class TestGreedy(unittest.TestCase):
    def test_greedy(self):
        result= greedy.iterativeActivitySelector(s,f)
        self.assertListEqual(result, correct)
        # another way to do test case
        self.assertListEqual(greedy.recursiveActivitySelector(s,f,-1,len(s)), correct)