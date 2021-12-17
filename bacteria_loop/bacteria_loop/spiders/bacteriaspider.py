import scrapy

class BacteriaSpider(scrapy.Spider):
    name = 'bacteria_loop'
    #allowed_domains = ['https://www.microbiologyresearch.org']
    start_urls =['https://www.microbiologyresearch.org/content/journal/ijsem/browse/']



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
            yield response.follow(article.get(), callback=self.parse_bacteria)      
        

    def parse_bacteria(self, response):
        '''
         # list of 10 unique bacteria species
        bacteria_species = ['Abditibacterium utsteinense',
                            'Abiotrophia defectiva',
                            'Abyssibacter profundi',
                            'Abyssicoccus albus',
                            'Abyssivirga alkaniphila',
                            'Acanthopleuribacter pedis',
                            'Acaricomes phytoseiuli',
                            'Acetanaerobacterium elongatum',
                            'Acetanaerobacterium sp.',
                            'Acetatifactor muris']
        '''
        bacteria_species = ['bac'] #test
        '''
        go through every element in HTML document and store it in results
        if one of the bacteria species appears inside 
        '''
        search_xpath = ("//p//text()[contains(., {0})]")
        for bact in bacteria_species:
            searchfor = search_xpath.format('"' + bact + '"')
            print(searchfor)
            results =  response.xpath(searchfor).getall() 
            for item in results:
                yield{
                    "bacteria_species" : bact,
                    "URL" : response.request.url,
                    "article" : item
                        }

        # Result: Approach fails due to dynamically loading websites and tags within elements
                      