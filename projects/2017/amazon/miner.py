#!/usr/bin/env python
from amazon.api import AmazonAPI
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG

def sample_lookup(asin):
    amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY,
                       AMAZON_ASSOC_TAG, region="US")
    product = amazon.lookup(ItemId=asin)
    return product
