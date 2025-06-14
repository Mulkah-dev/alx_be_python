import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,4),6)
        self.assertEqual(self.calc.add(5,6),11)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5,3),2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(5,3),15)

    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10,0))

    

if __name__ == '__main':
    unittest.main()