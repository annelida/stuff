#!/usr/bin/env python
from amazon.api import AmazonAPI
from amazon_scraper import AmazonScraper
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG


def sample_lookup(asin):
    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                       AMAZON_ASSOC_TAG, region="US")
    product = amazon.lookup(ItemId=asin)
    return product


def sample_scraper(asin):
    amzn = AmazonScraper(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                         AMAZON_ASSOC_TAG, Region='US', MaxQPS=0.9,
                         Timeout=5.0)
    product = amzn.lookup(ItemId=asin)
    return product
