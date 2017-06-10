import unittest
from square import square


class SquareTest(unittest.TestCase):
    def test(self):
        self.assertEqual(square(2), 4)

    def test_negative(self):
        self.assertEqual(square(-2), 4)

    def test_float(self):
        self.assertEqual(square(2.0), 4)

    def test_float_negative(self):
        self.assertEqual(square(-2.0), 4)

    def test_strings(self):
        """
        Test the square of 'str' returns the error
        """
        with self.assertRaises(TypeError):
            square('2', '-2', '2.0', '-2.0')



