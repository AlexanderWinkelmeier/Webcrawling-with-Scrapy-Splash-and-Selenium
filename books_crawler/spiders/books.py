# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    rules = (Rule(LinkExtractor(), callback='parse_page', follow=False),)
            # LinkExtractor extrahiert alle Links aus einer Webpage
            # erlaubt hierbei nur links mit 'music' in der Url duch "allow='music" als Argument des LinkExtractors
            # dann wird darüber mit parse_page geparsed
            # dann wird auf die nächste Seite gegangen (mit follow = True)
            # usw.
    def parse_page(self, response):
        yield {'URL': response.url}
        
