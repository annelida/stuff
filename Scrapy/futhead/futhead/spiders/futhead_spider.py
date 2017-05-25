import scrapy
from futhead.items import FutheadItem


class FutheadSpider(scrapy.Spider):
        name = "futhead"
        allowed_domains = ["futhead.com"]
        max_pages = 50
        
        def start_requests(self):
                for i in range(self.max_pages):
                        yield scrapy.Request('http://www.futhead.com/17/players/?page=%d&level=all_nif&bin_platform=ps' % i, callback=self.parse)

        def parse(self, response):
            self.logger.info('Visited on catalogues page %s', response.url)
            players_page_link = response.xpath('//div[contains(@class, "content")]/a[contains(@class, "display-block")]/@href').extract()
            for link in players_page_link:
                self.logger.debug('The items link is %s' % (link, ))
                url = response.urljoin(link)
                self.logger.debug('The players page absolute url is %s' % (url))
                yield scrapy.Request(url, callback=self.parse_players_page_content)
            # try:
            #         next_page = response.xpath('//span[contains(@class, "font-12 font-bold margin-l-r-10")]/following::a/@href').extract()[0]
            #         next_page_url = response.urljoin(next_page)
            #         self.logger.debug('This is next players page absolute url %s' % (next_page_url))
            #         yield scrapy.Request(next_page_url, self.parse)
            # except:
            #         pass

        def parse_players_page_content(self, response):
            self.logger.info('Players page parse function on %s' % (response.url, ))
            item = FutheadItem()
            item['Name'] = response.xpath('//div[@class="playercard-name"]/text()').extract()[0]
            item['Club'] = response.xpath('//a[@class="futhead-link"]/text()').extract()[0]
            item['League'] = response.xpath('//a[@class="futhead-link"]/text()').extract()[1]
            item['Nation'] = response.xpath('//a[@class="futhead-link"]/text()').extract()[2]
            item['SkillMoves'] = map(unicode.strip, response.xpath('//div[contains(@class, "col-xs-5 player-sidebar-value")]/text()[normalize-space()]').extract())[0]
            item['WeakFoot'] = map(unicode.strip, response.xpath('//div[contains(@class, "col-xs-5 player-sidebar-value")]/text()[normalize-space()]').extract())[1]
            item['StrongFoot'] = map(unicode.strip, response.xpath('//div[contains(@class, "col-xs-5 player-sidebar-value")]/text()[normalize-space()]').extract())[2]
            item['Age'] = map(unicode.strip, response.xpath('//div[contains(@class, "col-xs-5 player-sidebar-value")]/text()[normalize-space()]').extract())[3]
            item['Height'] = map(unicode.strip, response.xpath('//div[contains(@class, "col-xs-5 player-sidebar-value")]/text()[normalize-space()]').extract())[4]
            item['Workrates'] = map(unicode.strip, response.xpath('//div[contains(@class, "col-xs-5 player-sidebar-value")]/text()[normalize-space()]').extract())[5]
            item['Pace'] = response.xpath('//span[@class="chembot-delta"]/@data-chembot-base').extract()[0]
            item['Shooting'] = response.xpath('//span[@class="chembot-delta"]/@data-chembot-base').extract()[1]
            item['Passing'] = response.xpath('//span[@class="chembot-delta"]/@data-chembot-base').extract()[2]
            item['Dribbling'] = response.xpath('//span[@class="chembot-delta"]/@data-chembot-base').extract()[3]
            item['Defending'] = response.xpath('//span[@class="chembot-delta"]/@data-chembot-base').extract()[4]
            item['Physical'] = response.xpath('//span[@class="chembot-delta"]/@data-chembot-base').extract()[5]
            item['AttackerRating'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[0]
            item['CreatorRating'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[1]
            item['DefenderRating'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[2]
            item['BeastRating'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[3]
            item['HeadingRating'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[4]
            item['TotalStats'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[5]
            item['TotalLigs'] = response.xpath('//span[contains(@class, "player-stat-chembot chembot-delta")]/@data-chembot-base').extract()[6]
            item['Rating'] = response.xpath('//div[@class = "playercard-rating"]/text()').extract()
            item['Position'] = response.xpath('//div[@class = "playercard-position"]/text()').extract()
            yield item
            
            


        
            
                
