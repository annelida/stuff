import scrapy
from activesport.items import ActivesportItem
import logging
from scrapy.utils.log import configure_logging


configure_logging(install_root_handler=False)
logging.basicConfig(
    filename='log.txt',
    format='%(levelname)s: %(message)s',
    level=logging.INFO
)

"""
Go to the first categories page (such as Bikes and Frames)
Parse data out from categories page
Go to the each link to subcategories (such as Bikes, Frames, Scooters)
Parse data out from subcategories page
Go to the each link to item's page
Parse data out from item's page
Go to the next subcategories page if it exists
"""


class ActivesportSpider(scrapy.Spider):
    name = "activesport"
    allowed_domains = ["activesport.co"]
    # list of categories
    start_urls = [
        "http://activesport.co/epages/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e.sf/en_GB/?ObjectPath=/Shops/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e/Categories/Bikes_Frames", ]
    #     "http://activesport.co/epages/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e.sf/en_GB/?ObjectPath=/Shops/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e/Categories/Accessories",
    #     "http://activesport.co/epages/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e.sf/en_GB/?ObjectPath=/Shops/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e/Categories/Components",
    #     "http://activesport.co/epages/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e.sf/en_GB/?ObjectPath=/Shops/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e/Categories/Apparel",
    #     "http://activesport.co/epages/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e.sf/en_GB/?ObjectPath=/Shops/80c85f8f-7a95-4b1c-9c30-e64b314f3f2e/Categories/Tech"
    # ]

    sub_categories_number = 0

    def parse(self, response):
        """Retrieve data out from section's catalogue - the subcategories level"""
        self.logger.info('Visited on sections catalogue %s', response.url)
        # Extract link to the second level section, follow them
        list_of_subcatalogues = response.xpath(
            '//div[@class="InfoArea"]/h3/a/@href').extract()[:1]
        length = len(list_of_subcatalogues)
        sub_categories_number = + length
        self.logger.debug('List of subcategories has %s links' % (length,))
        for link in list_of_subcatalogues:
            self.logger.debug('The subcategories url %s' % (link, ))
            url = response.urljoin(link)
            self.logger.debug('The absolute subcategoties url is %s' % (url, ))
            yield scrapy.Request(url, callback=self.parse_subcategories_level)
        self.logger.debug('There are %s subcategories there' %
                          (sub_categories_number, ))

    def parse_subcategories_level(self, response):
        """Retrieve data out from subcategories levels"""
        self.logger.info('We are in subcategories level %s', response.url)
        # Extract link to the sub_subcategories, follow them
        try:
            list_of_sub_subcategories = response.xpath(
                '//h3[not(@class)]/a/@href').extract()
            length = len(list_of_sub_subcategories)
            self.logger.debug(
                'List of sub-subcategories has %s links' % (length,))
            for link in list_of_sub_subcategories:
                self.logger.debug(
                    'The sub-subcategories url is  %s' % (link, ))
                url = response.urljoin(link)
                self.logger.debug(
                    'The sub-subcategories absolute url is %s' % (url, ))
                yield scrapy.Request(url, callback=self.parse_item_follow_next_page)
        except:
            pass

    def parse_item_follow_next_page(self, response):
        """" Retrieve data from sub-subcategories level - items link, next page link"""
        self.logger.info('We are in sub-subcategories level %s', response.url)
        items_link = response.xpath(
            '//div[@class="InfoArea"]/h3[@class="TopPaddingWide"]/a/@href').extract()
        for link in items_link:
            self.logger.debug('The items link is %s' % (link, ))
            url = response.urljoin(link)
            self.logger.debug('The items pages absolute url is %s' % (url))
            yield scrapy.Request(url, callback=self.parse_item_content)
            # Going to the next items page if it exists
        try:
            next_page = response.xpath(
                '//ul[@class="PagerSizeContainer"]/li/a[@title="Next"]/@href').extract()[0]
            next_page_url = response.urljoin(next_page)
            self.logger.debug(
                'This is next items pages absolute url %s' % (next_page_url))
            yield scrapy.Request(next_page_url, self.parse_item_follow_next_page)
        except:
            pass

    def parse_item_content(self, response):
        """Extract all data about the particular item"""
        self.logger.info('Item parse function on %s' % (response.url, ))
        item = ActivesportItem()
        item['title'] = response.xpath(
            '//div[contains(@class, "InfoArea")]/h1/text()').extract()
        price = response.xpath(
            '//span[(@itemprop="price")]/text()').extract()
        item['price'] = price[0] if price else None
        link = response.xpath(
            '//li[contains(@style, "margin-bottom")]/a/@href').extract()
        item['link'] = link[0] if link else None
        # Items description can have several values
        desc1 = map(unicode.strip, response.xpath('//div[@id="tab-additional_information"]//text()[normalize-space()]').extract())
        desc2 = map(unicode.strip, response.xpath(
            '//div[@class="description"]//ul[not(@id="list1")]/li//text()[normalize-space()]').extract())
        desc3 = map(unicode.strip, response.xpath(
            '//div[contains(@style, "color")]/text()[normalize-space()]').extract())
        desc4 = map(unicode.strip, response.xpath('//div[@class="description"]//td//text()[normalize-space()]').extract())
        desc5 = map(unicode.strip, response.xpath(
            '//div[@class="description"]//p//text()[normalize-space()]').extract())
       
        if desc1:
            item['description'] = str(desc1).split(']')[0]
        elif desc2:
            item['description'] = str(desc2).split(']')[0]
        elif desc3:
            item['description'] = str(desc3).split(']')[0]
        elif desc4:
            item['description'] = str(desc4).split(']')[0]
        elif desc5:
            item['description'] = str(desc5).split(']')[0]    
        else:
            item['description'] = None

        yield item
