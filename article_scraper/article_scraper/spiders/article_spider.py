import scrapy


class BacteriaSpider(scrapy.Spider):
    name = 'article_spider'
    start_urls = ['https://www.microbiologyresearch.org/content/journal/ijsem/browse']


    '''
    headers ={
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'JSESSIONID=yPwOSrO7Cva2g87z7YYJB-T-.mbslive-10-240-10-13; cb-enabled=enabled; _ga=GA1.2.638163648.1638526331; _gid=GA1.2.2114249282.1639415830; JSESSIONID=d3g5D1LEGObsRQEB3HqSEsEW.mbslive-10-240-10-13; _gat_gtag_UA_48529861_1=1; __atuvc=3%7C48%2C16%7C49%2C12%7C50; __atuvs=61ba353719d78ac4006; AWSALB=9w4auiZdNcIBBJ9KPdQY+IMYRYvqdgrVtIEs7xF7g68+B+xUnE2hv6Hb+ysYWFhgcLWgpgc2wExaxIYxi4F5ZOOO2yorrllwlRqOCY7ackOyuwRV/6GowfCZ8I2E; AWSALBCORS=9w4auiZdNcIBBJ9KPdQY+IMYRYvqdgrVtIEs7xF7g68+B+xUnE2hv6Hb+ysYWFhgcLWgpgc2wExaxIYxi4F5ZOOO2yorrllwlRqOCY7ackOyuwRV/6GowfCZ8I2E',
        'pragma': 'no-cache',
        'referer': 'https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004987',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    #allowed_domains = ['https://www.microbiologyresearch.org']
    start_urls =['https://www.microbiologyresearch.org/content/journal/ijsem/browse/']
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
    '''
    def parse_content(self, response):
        url = 'https://www.microbiologyresearch.org/docserver/ahah/fulltext/ijsem/71/9/ijsem004987.html?expires=1639655975&id=id&accname=guest&checksum=7042A8DAEF537A2C540C6578D7606F41'

        yield scrapy.Request(url, callback=self.parse_api, headers=self.headers)
        

    def parse_api(self, reponse):
        
    
    # I am trying to figure out how to get to the content of the articles of the dynamic website via 'accept : */*'. 
    # Most tutorials only deal with the json approach.
    