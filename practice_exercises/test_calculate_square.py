import unittest
from calculate_square import square

class TestSquareFunction(unittest.TestCase):
    def test_square_of_number(self):
        self.assertEqual(square(4), 16)

if __name__ == '__main__':
    unittest.main()