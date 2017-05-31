#!/usr/bin/env python
import unittest
from miner import sample_lookup


class InitialTest(unittest.TestCase):
    """Test how it works out from the box"""

    def setUp(self):
        self.product = sample_lookup('B00EOE0WKQ')

    def test_simple_query_number_properties(self):
        self.assertEqual(len(dir(self.product)), 93)
