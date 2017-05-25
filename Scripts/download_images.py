import urllib
import time

f = open('img_urls.csv')
for url in f:
    url = url.strip()
    resource = urllib.urlopen(url)
    time.sleep(20)
    filename = url.split("//")[-2].replace('/''.') + '.jpg'
    output = open(filename, "wb")
    # output = open("file01.jpg", "wb")
    output.write(resource.read())
    output.close()



