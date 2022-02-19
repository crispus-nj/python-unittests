import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(20, 5)
        self.assertEqual(result, 25)
    
    def test_mutliple(self):
        result = calc.multiply(20, 5)
        self.assertEqual(result, 100)
    
    def test_subtract(self):
        self.assertEqual(calc.subtract(20, 5), 15)
        self.assertEqual(calc.subtract(20, 10), 10)
    
    def test_divide(self):
        self.assertEqual(calc.divide(20, 2), 10)

        # testing exceptions using context manager
        with self.assertRaises(ValueError):
            calc.divide(20, 0)

if __name__ == "__main__":
    unittest.main()

# python3 -m unittest test_calc.py