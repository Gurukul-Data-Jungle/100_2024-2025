import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from class24 import searchMatrix
import unittest

class testFunc(unittest.TestCase):
    def testCases1(self):        
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 5), True)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 30), True)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1), True)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60), True)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 6), False)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0), False)
        self.assertEqual(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61), False)
    
    def testCases2(self):
        self.assertEqual(searchMatrix([[1, 3, 5, 7]], 5), True)
        self.assertEqual(searchMatrix([[1, 3, 5, 7]], 4), False)
    
    def testCase3(self):
        self.assertEqual(searchMatrix([[1]], 1), True)
        self.assertEqual(searchMatrix([[1]], 0), False)
    
    def testCase4(self):
        self.assertEqual(searchMatrix([[]], 1), False)
        self.assertEqual(searchMatrix([[]], 10), False)

if __name__ == '__main__':
    unittest.main()
    