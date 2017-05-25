import os
import requests
import logging
import time

logger = logging.getLogger('thumbnails')
hdlr = logging.FileHandler('thumbnails.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

f = open('img_urls.csv')
for url in f:
    url = url.strip()
    logger.info("This is images url: %s" % (url))
    resp = requests.get(url)
    img = resp.raw
    time.sleep(20)
    # save raw img on hard disc
    path = '/home/vikky/Desktop/DVCS/yann_decoopman/images/'
    filename = url.split('//')[-1].replace('/', '_') + '.jpg'
    logger.info("This is images file name: %s" % (filename))
    fullpath = os.path.join(path, filename)
    with open(filename, "wb") as img_file:
        img_file.write(resp.content)
        img_file.close()



