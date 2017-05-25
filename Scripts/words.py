# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv


options = webdriver.ChromeOptions()
options.add_argument('--lang=fr')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('http://www.google.fr')
# driver.get('http://www.google.com/xhtml')
time.sleep(5)
with open('words.csv', 'w') as file:
    writer = csv.writer(file, delimiter='\t', lineterminator='\n',)
    handle = open('marchands.txt')
    for keyword in handle:
        keyword = keyword.strip().decode('utf-8')
        search_box = driver.find_element_by_name('q')
        search_box.clear()
        search_box.send_keys(keyword)
        search_box.submit()
        time.sleep(5)
        html_source = driver.page_source.encode('utf-8')
        content = BeautifulSoup(html_source)
        all_links = content.find_all('h3', {"class": "r"})
        for link in all_links:
            atag = link.find_all('a')
            for atags in atag:
                # print (atags.get("href"))
                href = str(atags.get("href")).split(' ')
                writer.writerow([keyword.encode('utf-8'), href])
                                
driver.quit()


