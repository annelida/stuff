import scrapy


class CpkSpider(scrapy.Spider):
    name = "cpk"
    allowed_domains = ["zakon4.rada.gov.ua"]
    start_urls = [
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page2",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page3",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page4",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page5",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page6",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page7",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page8",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page9",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page10",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page11",
        "http://zakon4.rada.gov.ua/laws/show/1618-15/page12"]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
