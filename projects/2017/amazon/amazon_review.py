#!/usr/bin/env python
from amazon_scraper import AmazonScraper
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG
import itertools

amzn = AmazonScraper(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region='US', MaxQPS=0.9, Timeout=5.0)
p = amzn.lookup(ItemId='B0051QVF7A')
rs = p.reviews()
for r in rs.brief_reviews:
    print(r.id)
