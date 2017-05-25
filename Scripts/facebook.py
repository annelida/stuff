# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()
options.add_argument('--lang=fr')
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get('https://www.facebook.com/login')
# driver.get('http://www.google.com/xhtml')
login_email = driver.find_element_by_name("email")
login_email.send_keys("viqsiq@mail.ru")
time.sleep(5)
login_password = driver.find_element_by_name("pass")
login_password.send_keys("V!ku56*]")
time.sleep(5)
login_password.submit()
driver.get('https://www.facebook.com/search/858681357497101/likers')
# driver.get('https://www.facebook.com/')
time.sleep(15)
for i in xrange(5):
    driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    print(i)
    time.sleep(10)
html_source = driver.page_source.encode('utf-8')
content = BeautifulSoup(html_source)
with open('profile_link.csv', 'w') as file:
    writer = csv.writer(file, delimiter='\t', lineterminator='\n',)
    all_links = content.find_all('div', {"class": "_gll"})
    for link in all_links:
        atag = link.find_all('a')
        for atags in atag:
            print (atags.get("href"))
            href = str(atags.get("href")).split(' ')
            writer.writerow(href)
    with open('profile_name.csv', 'w') as file:
        writer = csv.writer(file, delimiter='\t', lineterminator='\n',)
        all_profile_names = content.find_all('div', {"class": "_5d-5"})
        for name in all_profile_names:
            print name.text
            profile_name = name.text.strip().encode('utf-8')
            writer.writerow([profile_name])
 
       
driver.quit()



