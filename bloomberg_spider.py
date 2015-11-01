import scrapy

class BloombergSpider(scrapy.Spider):
    name = 'bloomberg'
    start_urls = [
        'http://www.bloomberg.com/quote/AAPL:US',
        'http://www.bloomberg.com/quote/GOOGL:US',
        'http://www.bloomberg.com/quote/AMZN:US',
    ]

    def parse(self, response):
        for sel in response.css('meta'):
            itemprop = sel.css('::attr(itemprop)').extract()
            if itemprop:
                yield {
                    'itemprop': itemprop,
                    'content': sel.css('::attr(content)').extract(),
                }
