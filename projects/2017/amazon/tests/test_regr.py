#!/usr/bin/env python
import unittest
from amazon.miner import sample_lookup


class InitialTest(unittest.TestCase):
    """Test how it works out from the box"""

    def test_simple_query(self):
        product = sample_lookup('B00EOE0WKQ')
        self.assertEqual(dir(product), 86)
