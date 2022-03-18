import scrapy
from scrapy_requests import HtmlRequest
from SR.items import SrItem
from scrapy.loader import ItemLoader

class SrspiderSpider(scrapy.Spider):
    name = 'SRspider'
    start_urls =['https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004987']
    
    def parse(self, response):
        url = response.request.url
        yield HtmlRequest(url=url, callback=self.parse_title, render=True, options={'sleep': 1})
        
    def parse_title(self,response):
        loader = ItemLoader(item = SrItem(), selector=response)
        
        loader.add_xpath('title', "//h1[@class='item-meta-data__item-title']")
        loader.add_xpath('abstract', "//div[@class='articleSection article-abstract']/p")
        loader.add_xpath('paragraph', "//div[@class='articleSection']/p")

        yield loader.load_item()



'''
    def parse_title(self,response):
        yield {
            'title': response.xpath("string(//h1[@class='item-meta-data__item-title'])").get()
        }
        yield {
            'abstract': response.xpath("string(//div[@class='articleSection article-abstract']/p)").get()
            }
        for p in response.xpath("//div[@class='articleSection']/p"):
            yield {
                'paragraph': p.xpath('string(.)').get()
                }



    
        yield {
            #'abstract': response.xpath("string(//div[@class='articleSection article-abstract']/p)").get(),
            'fulltext': response.xpath("string(//div[@class='articleSection'][2]//p)").extract()
              }
    '''          


'''
    def parse(self, response):
        # get all volume links and follow them
        for volume in response.css('h3.h5 a::attr(href)'):
            yield response.follow(volume.get(), callback=self.parse_issues)
                
    def parse_issues(self, response):
            
        # get all issue links within a volume and follow them
        for issue in response.css('li.issue a::attr(href)'):
            yield response.follow(issue.get(), callback=self.parse_articles)

    def parse_articles(self, response): 

        # get all article links within a issue and follow them
        for article in response.css('span.articleTitle.js-articleTitle.title a::attr(href)'):
            yield response.follow(article.get(), callback=self.parse_content)      
        
    def parse_content(self, response):
        url = response.request.url
        yield HtmlRequest(url=url, callback=self.parse_header, render=True, options={'sleep': 1})

    def parse_header(self, response):
        yield {
            'title': response.xpath("//h1[@class='item-meta-data__item-title::text']", first=True)
        }
'''