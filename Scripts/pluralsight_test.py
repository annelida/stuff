from splinter import Browser
executable_path = {'executable_path': '/usr/lib/chromium-browser/chromedriver'}

browser = Browser('chrome', **executable_path)
browser.visit('http://google.com')
browser.fill('q', 'pluralsight')
browser.find_by_name('btnG').click()
all_links = browser.find_by_xpath('//h3[@class="r"]/a').first.value
print all_links
browser.quit()
