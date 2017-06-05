import unittest
from square import square


class SquareTest(unittest.TestCase):
    def test(self):
        self.assertEqual(square(2), 4)


class Square_negativeTest(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(square(-2), 4)


class Square_floatTest(unittest.TestCase):
    def test_float(self):
        self.assertEqual(square(2.0), 4)


class Square_negative_floatTest(unittest.TestCase):
    def test_float_negative(self):
        self.assertEqual(square(-2.0), 4)

