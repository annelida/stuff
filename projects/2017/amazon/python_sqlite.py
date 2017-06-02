#!/usr/bin/env python
from amazon_scraper import AmazonScraper
from settings import AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG
import sqlite3

amzn = AmazonScraper(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG, Region='US', MaxQPS=0.9, Timeout=5.0)
product = amzn.lookup(ItemId='B0051QVF7A')
a = product.asin
t = product.title


def sample_db():
    connection = sqlite3.connect('amazon_data.db')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS amazon_test_data")
    cursor.execute("CREATE TABLE amazon_test_data(asin VARCHAR(12), title TEXT);")
    cursor.execute("SELECT * FROM amazon_test_data WHERE asin=?", (a,))
    result = cursor.fetchone()
    if result:
        print("Item already in database: %s" % (a))
    else:
        cursor.execute("INSERT INTO amazon_test_data VALUES(?, ?);", (a, t))
    
        connection.commit()
        print("Item stored in database: %s" % (a))
sample_db()


