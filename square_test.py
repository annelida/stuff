import unittest
from square import square


class SquareTest(unittest.TestCase):
    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-2), 4)
        self.assertEqual(square(2.0), 4)
        self.assertEqual(square(-2.0), 4)
        with self.assertRaises(TypeError):
            square('2', '-2', '2.0', '-2.0')



