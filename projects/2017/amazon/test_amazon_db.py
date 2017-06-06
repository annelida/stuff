#!/usr/bin/env python
import unittest
import sqlite3


class TestAmazonDatabase(unittest.TestCase):
    """
    Setup a temporary database
    """
    def setup(self):
        self.item = [1, 'B00EOE0WKQ', 'Amazon Fire Phone, 32GB (AT&T)']
        self.connection = sqlite3.connect('amazon_data.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS amazon_product_data")
        self.cursor.execute("CREATE TABLE amazon_product_data(id INTEGER PRIMARY KEY AUTOINCREMENT, asin VARCHAR(12), title TEXT);")
        self.cursor.execute("INSERT INTO amazon_product_data VALUES(?, ?, ?);", (self.item))
        self.connection.commit()
        print("Item stored in database: %s" % (self.item))

    def test_product_table(self):
        """
        Tests product table
        """
        print(self.item)
        #self.assertTrue('amazon_product_data')


#    def tearDown(self):
        
