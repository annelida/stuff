import scrapy

"""
Go to the first page on each of 9 catalogues
Parse data out from catalogue's page
Go to the each link to item's page
Parse data out from item's page
Go to the next catalogue's page if it exists
"""



class IherbSpider(scrapy.Spider):
    name = "iherb"
    allowed_domains = ["iherb.com"]
    start_urls = [
        "http://www.iherb.com/Supplements",
        "http://www.iherb.com/Herbs",
        "http://www.iherb.com/Bath-Beauty#p=1",
        "http://www.iherb.com/Face-Lotions-Cream#p=1",
        "http://www.iherb.com/Food-Grocery-Items#p=1",
        "http://www.iherb.com/Children-s-Health#p=1",
        "http://www.iherb.com/Sports-Fitness-Athletic#p=1",
        "http://www.iherb.com/Healthy-Home#p=1"
    ]

    def parse(self, response):
        """Retrieve data out from catalogue's page"""
        self.logger.info('&Item parse function called on %s', response.url)
        items_names = response.xpath('//h1[@class="product__title"]/text()').extract()
        items_pages_links = response.xpath('//a[@class="image-link"]/@href').extract()
        items_data = zip(items_names, items_pages_links)
        for i in items_data:
            self.logger.info('&& Item name %s and link to they', (i[0], i[1]))
            yield scrapy.Request(i[1], self.parse_item)
        try:
            next_page = response.xpath('//span[@class="pagination-selected"]/following::a[@class="pagination-next"]/@href')
            url = response.urljoin(next_page.extract()[0])
            self.logger.debug('&&& This is a catalogue page: %s', next_page)
            yield scrapy.Request(url, self.parse)
        except:
            pass


        
    def parse_item(self, response):
        """Extract all data about the particular item"""
        self.logger.debug('&Item parse function called on %s', response.url)
        pass
