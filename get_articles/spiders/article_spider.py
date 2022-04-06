import scrapy
from scrapy_requests import HtmlRequest
from get_articles.items import GetArticlesItem
from scrapy.loader import ItemLoader
import pandas as pd


class ArticleSpiderSpider(scrapy.Spider):
    name = 'article_spider'
    df = pd.read_csv('D:/TH_Koeln/WS21-22/Bachelorarbeit/python_scripts/venv_scrapy-requests/cleaned_article_DOIs.csv')
    doi_list = df['doi'].tolist()

    start_urls = doi_list
    
    def parse(self, response):
        yield HtmlRequest(url=response.url, callback=self.parse_content, render=True, options={'sleep': 1})

    def parse_content(self, response):
        loader = ItemLoader(item = GetArticlesItem(), selector=response)

        loader.add_value('url', response.url)

        loader.add_xpath('title', "//h1[@class='item-meta-data__item-title']")

        loader.add_xpath('abstract', "//div[@class='articleSection article-abstract']/p")
        loader.add_xpath('abstract', "//div[@class='articleabstract']/div/div[@class='description']/p")

        loader.add_xpath('fulltext', "//div[@class='articleSection']/p")
        loader.add_xpath('fulltext', "//div[@class='articleSection']/div/p") # texte mit mehreren überschriften und paragraphen im volltext
        
        yield loader.load_item()