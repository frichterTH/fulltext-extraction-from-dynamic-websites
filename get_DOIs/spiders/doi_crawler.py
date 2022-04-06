import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoiCrawlerSpider(CrawlSpider):
    name = 'doi_crawler'
    allowed_domains = ['www.microbiologyresearch.org']
    start_urls = ['https://www.microbiologyresearch.org/content/journal/ijsem/browse']

    volume_links = LinkExtractor(restrict_xpaths="//h3[@class='h5']/a")
    issue_links = LinkExtractor(restrict_xpaths="//ul[@class='togglecontent list-unstyled volume-issue-list']/li[@class='issue']/a")
    page_links = LinkExtractor(restrict_xpaths="//div[@class='paginator pull-left']/a")

    rules = (
        Rule(volume_links, follow=True),
        Rule(issue_links, callback='parse_item', follow=True),
        Rule(page_links, callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        yield {
            'doi': response.css('div.articleSourceTag a::attr(href)').getall()
                }
