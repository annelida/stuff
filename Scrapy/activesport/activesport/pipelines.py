# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
import logging


# Create a table, takes the Item and add it into scrapedata.db
class ActivesportPipeline(object):

    def __init__(self):
        msg = '%%s %s pipeline step' % (self.__class__.__name__,)
        self.connection = sqlite3.connect('./scrapy_data.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS activesport(id INTEGER PRIMARY KEY,
                                                                    title TEXT, price REAL, link VARCHAR(50), description TEXT)""")
        logging.debug(msg % 'executing first')
        
    # Take the item and put it in database - do not allow duplicates
    def process_item(self, item, spider):

        self.cursor.execute(
            "SELECT * FROM activesport WHERE title=?", item['title'])
        result = self.cursor.fetchone()
        if result:
            logging.debug("Item already in database: %s" % (item))
        else:
            self.cursor.execute("INSERT INTO activesport(title, price, link, description) VALUES(?,?,?, ?)", (item[
                                'title'][0], item['price'], item['link'], item['description']))

            self.connection.commit()

            logging.debug("Item stored :" % (item))
        return item
