# -*- coding: utf-8 -*-
import scrapy
from mareduc.items import MareducItem


class MareducSpider(scrapy.Spider):
    name = "mareduc"
    allowed_domains = ["www.ma-reduc.com"]
    start_urls = ["https://www.ma-reduc.com/liste-des-sites-A.php",
                  "https://www.ma-reduc.com/liste-des-sites-B.php",
                  "https://www.ma-reduc.com/liste-des-sites-C.php",
                  "https://www.ma-reduc.com/liste-des-sites-D.php",
                  "https://www.ma-reduc.com/liste-des-sites-E.php",
                  "https://www.ma-reduc.com/liste-des-sites-F.php",
                  "https://www.ma-reduc.com/liste-des-sites-G.php",
                  "https://www.ma-reduc.com/liste-des-sites-H.php",
                  "https://www.ma-reduc.com/liste-des-sites-I.php",
                  "https://www.ma-reduc.com/liste-des-sites-J.php",
                  "https://www.ma-reduc.com/liste-des-sites-K.php",
                  "https://www.ma-reduc.com/liste-des-sites-L.php",
                  "https://www.ma-reduc.com/liste-des-sites-M.php",
                  "https://www.ma-reduc.com/liste-des-sites-N.php",
                  "https://www.ma-reduc.com/liste-des-sites-O.php",
                  "https://www.ma-reduc.com/liste-des-sites-P.php",
                  "https://www.ma-reduc.com/liste-des-sites-Q.php",
                  "https://www.ma-reduc.com/liste-des-sites-R.php",
                  "https://www.ma-reduc.com/liste-des-sites-S.php",
                  "https://www.ma-reduc.com/liste-des-sites-T.php",
                  "https://www.ma-reduc.com/liste-des-sites-U.php",
                  "https://www.ma-reduc.com/liste-des-sites-V.php",
                  "https://www.ma-reduc.com/liste-des-sites-W.php",
                  "https://www.ma-reduc.com/liste-des-sites-X.php",
                  "https://www.ma-reduc.com/liste-des-sites-Y.php",
                  "https://www.ma-reduc.com/liste-des-sites-Z.php",
                  ]
 
    def parse(self, response):
        self.logger.info('Visited on catalogues page %s', response.url)
        merchants_page_link = response.xpath('//a[contains(@class, "font-90")]/@href').extract()
        for link in merchants_page_link:
            self.logger.debug('The mercants pages link is %s' % (link, ))
            url = response.urljoin(link)
            self.logger.debug('The merchants pages absolute url is %s' % (url))
            yield scrapy.Request(url, callback=self.parse_item)
        try:
            next_page = response.xpath('//a[@class="nav-next"]/@href').extract()[0]
            next_page_url = response.urljoin(next_page)
            self.logger.debug('This is next merchants page absolute url %s' % (next_page_url))
            yield scrapy.Request(next_page_url, self.parse)
        except:
            pass

    def parse_item(self, response):
        self.logger.info('Visited on items page %s', response.url)
        item = MareducItem()
        item['merchant'] = response.xpath('//div[@class="text-center"]/img[contains(@class, "unveil")]/@alt').extract()
        item['merchant_link'] = response.url
        item['similar_category'] =  response.xpath('//div[@id="block-similar-categories"]//li/a/text()').extract()
        item['simcat_link'] = response.xpath('//div[@id="block-similar-categories"]//li/a/@href').extract()
        yield item

