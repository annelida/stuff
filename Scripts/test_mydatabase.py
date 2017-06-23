import os
import unittest
import sqlite3


class TestMyDatabase(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect("mydatabase.db")
        print("Opened database successfully")

        conn.execute("DROP TABLE IF EXISTS COMPANY")
        conn.execute('''CREATE TABLE COMPANY
                 (ID INT PRIMARY KEY   NOT NULL,
                 NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50),SALARY         REAL);''')
        print("Table created successfully")
        conn.close()

    def tearDown(self):
        os.remove("mydatabase.db")
