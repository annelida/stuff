#!/usr/bin/env python
import unittest
from miner import sample_lookup, sample_scraper
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
        names = ['actors', 'api', 'asin', 'author', 'authors', 'availability',
                 'availability_max_hours', 'availability_min_hours', 'availability_type',
                 'aws_associate_tag', 'binding', 'brand', 'browse_nodes',
                 'color', 'creators', 'detail_page_url', 'directors', 'ean', 'edition',
                 'editorial_review', 'editorial_reviews', 'eisbn', 'features',
                 'formatted_price', 'genre', 'get_attribute', 'get_attribute_details',
                 'get_attributes', 'get_parent', 'images', 'is_adult', 'is_preorder',
                 'isbn', 'label', 'languages', 'large_image_url', 'list_price',
                 'manufacturer', 'medium_image_url', 'model', 'mpn', 'offer_id',
                 'offer_url', 'pages', 'parent', 'parent_asin', 'parsed_response',
                 'part_number', 'price_and_currency', 'product_group', 'product_type_name',
                 'publication_date', 'publisher', 'region', 'release_date', 'reviews',
                 'running_time', 'sales_rank', 'sku', 'small_image_url', 'studio',
                 'tiny_image_url', 'title', 'to_string', 'upc']
        for name in names:
            self.assertTrue(name in dir(self.product), name)

    def tearDown(self):
        del(self.product)


class InitialAmazonScraperTest(unittest.TestCase):
    """How scraper works out from the box"""

    def setUp(self):
        self.product = sample_scraper('B00EOE0WKQ')

    def test_simple_query_number_properties(self):
        self.assertEqual(len(dir(self.product)), 39)

    def test_properties_names(self):
        names = ['alternatives', 'api', 'author_bio', 'author_page_url', 'product',
                 'ratings', 'reviews', 'reviews_url', 'soup', 'supplemental_text',
                 'to_dict', 'url']
        for name in names:
            self.assertTrue(name in dir(self.product))

    def tearDown(self):
        del(self.product)
