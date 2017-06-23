import os
import unittest
import sqlite3


class TestMyDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect("mydatabase.db")
        print("Opened database successfully")

        self.conn.execute("DROP TABLE IF EXISTS COMPANY")
        self.conn.execute('''CREATE TABLE COMPANY
                 (ID INT PRIMARY KEY   NOT NULL,
                 NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50),SALARY         REAL);''')
        print("Table created successfully")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (1, 'Paul', 32, 'California', 20000.00 )")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
        self.conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
              VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00 )")
        print("Records created successfully")
        self.conn.commit()

    def test_search_entries(self):
        cursor = self.conn.execute("SELECT id, name, address, salary from COMPANY")
        for row in cursor:
            print "ID = ", row[0]
            print "NAME = ", row[1]
            print "ADDRESS = ", row[2]
            print "SALARY = ", row[3], "\n"

        print("Operation done successfully")


    def tearDown(self):
        os.remove("mydatabase.db")
