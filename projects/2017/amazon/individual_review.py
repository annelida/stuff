#!/usr/bin/env python
from amazon_scraper import AmazonScraper
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG
import itertools

amzn = AmazonScraper(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region='US', MaxQPS=0.9, Timeout=5.0)

review_id = 'R3MF0NIRI3BT1E'
r = amzn.review(Id=review_id)
print(r.asin, r.rating, r.title, r.url, r.date, r.text, r.user)
print(dir(r))
