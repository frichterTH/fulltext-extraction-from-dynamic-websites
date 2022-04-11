# fulltext-extraction-from-dynamic-websites
Full text (articles) extraction from dynamic websites using a web scraping approach.

First I scraped the DOIs of all articles found on IJSEM.
Then I convert them to a list and gave it as start_urls for the next python script. 
It scrapes the URL, the title, the abtract and the fulltext of all DOIs.

In the next step I'm trying to use spaCy to extract all bacteria in the articles and at least one related property.
