# fulltext-extraction-from-dynamic-websites
Full text (articles) extraction from dynamic websites using a web scraping approach.

First I scraped the DOIs of all articles found on IJSEM and saved it in a CSV.
Then I converted the CSV to a list and gave it as start_urls for the python script article_scraper in the scrapy project get_articles. 
It scrapes the URL, the title, the abtract and the fulltext of all DOIs, if available.
