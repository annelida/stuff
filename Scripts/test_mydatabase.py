import os
import unittest
import sqlite3


class TestMyDatabase(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect("mydatabase.db")
    print("Opened database successfully")

    def tearDown(self):
        os.remove("mydatabase.db")
