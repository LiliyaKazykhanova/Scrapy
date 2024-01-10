# Scraping Job Postings
### by Liliya Kazykhanova

Web Scraping Job Postings from: `https://jobs.steward.org`

***
Web scraping is a powerful tool for data science, as it allows businesses to collect and analyze data from different sources quickly and cost-effectively.

**Task**: Python Scrapy spider that scrapes Jobs data from jobs.steward.org.

These scraper extracts the following fields from jobs pages:

* Job ID
* Job title
* Location
* Job type 
* Date posted
* Date scraped
* Job description
* Url address

**Parameters**

```python
custom_settings = {
    'DOWNLOAD_DELAY': 2, # 2 seconds of delay
    'RANDOMIZE_DOWNLOAD_DELAY': True
    }
```
***
#### **Storing the scraped data**
Write command in CMD

```
scrapy runspider steward.py -o steward_job_data.json
```
```
steward_job_data.json
```
***
