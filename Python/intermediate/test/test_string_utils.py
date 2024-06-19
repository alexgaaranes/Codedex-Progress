from string_utils import *
import unittest

class TestStringUtils(unittest.TestCase):

    def test_reverse(self):
       result_string = reverse_string("Hello")

       expected_string = "olleH"
       self.assertEqual(result_string, expected_string)

    def test_capitalize(self):
        result_string = capitalize_string("walmart")

        expected_string = "Walmart"
        self.assertEqual(result_string, expected_string)

    def test_is_capitalize(self):
        result_bool = is_capitalized("Hello")

        self.assertTrue(result_bool)


if __name__ == '__main__':
    unittest.main()
