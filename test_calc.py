import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        result = calc.add(20, 5)
        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()