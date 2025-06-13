import unittest
from find_max import find_maximum

class TestFindMaximum(unittest.TestCase):
    def test_maximum_of_numberA(self):
        self.assertEqual(find_maximum(3,2), 3)
                           
    def test_maximum_of_numberB(self):
        self.assertEqual(find_maximum(2,3), 3)

if __name__ == '__main__':
    unittest.main()


