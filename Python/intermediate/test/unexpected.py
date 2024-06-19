import unittest
import math

def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestUnexpected(unittest.TestCase):
    
    def test_get_sqrt(self):
        x = get_sqrt(169)
        self.assertEqual(x, 13)

        with self.assertRaises(ValueError):
            self.assertEqual(get_sqrt(-100), 10)

    def test_divide(self):
        y = divide(35,7)
        self.assertEqual(y,5)

        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(divide(42,0),6)

if __name__ == '__main__':
    unittest.main()

