import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BacteriaBroadSpider(CrawlSpider):
    name = 'bacteria_broadcrawl'
    allowed_domains = ['https://www.microbiologyresearch.org/content/journal/ijsem']
    start_urls = ['https://www.microbiologyresearch.org/content/journal/ijsem/browse']

    bacteria_details = LinkExtractor(restrict_css='li.a')

    rule_bacteria_details = Rule(bacteria_details, callback='parse_item', follow=False)

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    # approach stopped when trying to get to the desired page via several specific links to scrape artel there
