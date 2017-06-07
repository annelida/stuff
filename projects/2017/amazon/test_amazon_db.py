#!/usr/bin/env python
import unittest
import sqlite3
import os


class TestAmazonDatabase(unittest.TestCase):
    """
    Setup a temporary database
    """

    def setUp(self):
        self.item = [1, 'B00EOE0WKQ', 'Amazon Fire Phone, 32GB (AT&T)']
        self.review = [1,
                       'RFITH44V8SLM9',
                       'KK84',
                       'Love my Amazon Fire I was already a Prime member so using it to watch my videos, play music and shop from my phone was all great. Phone stood up to the abuse very well and it finally died (battery issue) after over 3 years. Wish they would come out with an updated version! Phone was very user friendly way more than the I-Phone. It did lack in content as far as apps go but was getting better. battery life was great when new then slowly got worse over time probably due to me charging every night regardless of how much battery life it still had. Would buy a new version in a heart beat especially if they gave me another free year of prime and improved upon an already great phone.']
        self.connection = sqlite3.connect('amazon_data.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS amazon_product_data")
        self.cursor.execute(
            "CREATE TABLE amazon_product_data(id INTEGER PRIMARY KEY AUTOINCREMENT, asin VARCHAR(12), title TEXT);")
        self.cursor.execute(
            "INSERT INTO amazon_product_data VALUES(?, ?, ?);",
            (self.item))
        self.connection.commit()
        print("Item stored in database: %s" % (self.item))

    def test_product_table(self):
        """
        Tests product table
        """
        print(self.item)
        # self.assertTrue('amazon_product_data')

    def test_review_table(self):
        print(self.review)

    def tearDown(self):
        """
        Delete the database
        """
        os.remove("amazon_data.db")
