from crawl4ai.spiders import CrawlSpider
from crawl4ai.items import BaseItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class KeneseAccentSpider(CrawlSpider):
    name = 'kenese_accent'
    allowed_domains = ['kenese.accenthotels.com']
    start_urls = ['https://kenese.accenthotels.com/hu']

    rules = (
        # Follow internal links within the domain
        Rule(LinkExtractor(allow_domains=allowed_domains), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        item = BaseItem()
        item['url'] = response.url
        # Extract the page title
        item['title'] = response.css('title::text').get()
        # Extract text content, paragraphs etc.
        item['content'] = ' '.join(response.css('p::text, li::text, div::text').getall()).strip()
        yield item
