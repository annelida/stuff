#!/usr/bin/env python
import unittest
from miner import sample_lookup
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG

class CredentialTest(unittest.TestCase):

    def test_credentials_not_empty(self):
        self.assertTrue(AMAZON_ACCESS_KEY, "Amazon access key is empty")
        self.assertTrue(AMAZON_SECRET_KEY, "Amazon secret key is empty")
        self.assertTrue(AMAZON_ASSOC_TAG, "Amazon associated tag is empty")
    

class InitialAmazonAPITest(unittest.TestCase):
    """Test how it works out from the box"""

    def setUp(self):
        self.product = sample_lookup('B00EOE0WKQ')

    def test_simple_query_number_properties(self):
        self.assertEqual(len(dir(self.product)), 93)

    def test_properties_names(self):
        names = ['alternatives', 'api', 'author_bio', 'author_page_url', 'product',
                 'ratings', 'reviews', 'reviews_url', 'soup', 'supplemental_text',
                 'to_dict', 'url']
        self.assertTrue(dir(names in dir(self.product)))

    def tearDown(self):
        del(self.product)

