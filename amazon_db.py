#!/usr/bin/env python
from amazon_scraper import AmazonScraper
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG
import sqlite3

amzn = AmazonScraper(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region='US', MaxQPS=0.9, Timeout=5.0)
product = amzn.lookup(ItemId='B0051QVF7A')
item = [1, product.asin, product.title]


def sample_db():
    connection = sqlite3.connect('amazon_data.db')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS amazon_product_data")
    cursor.execute("CREATE TABLE amazon_product_data(id INTEGER PRIMARY KEY AUTOINCREMENT, asin VARCHAR(12), title TEXT);")
    cursor.execute("INSERT INTO amazon_product_data VALUES(?, ?, ?);", (item))
    connection.commit()
    print("Item stored in database: %s" % (item))
sample_db()

