#!/usr/bin/env python
import unittest
import sqlite3


class TestAmazonDatabase(unittest.TestCase):
    """
    Setup a temporary database
    """
    def setup(self):
        item = [1, 'B00EOE0WKQ', 'Amazon Fire Phone, 32GB (AT&T)']
        connection = sqlite3.connect('amazon_data.db')
        cursor = connection.cursor()
        cursor.execute("DROP TABLE IF EXISTS amazon_product_data")
        cursor.execute("CREATE TABLE amazon_product_data(id INTEGER PRIMARY KEY AUTOINCREMENT, asin VARCHAR(12), title TEXT);")
        cursor.execute("INSERT INTO amazon_product_data VALUES(?, ?, ?);", (item))
        connection.commit()
        print("Item stored in database: %s" % (item))

    
