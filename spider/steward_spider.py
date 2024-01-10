import scrapy
from datetime import date, datetime


class StewardSpider(scrapy.Spider):
    # name of the spider
    name = 'steward_spider'
    today = date.today().isoformat()
    start_urls = ["https://jobs.steward.org/joblist?page_size=50&page_number=1&sort_by=headline&sort_order=ASC"]
    
    custom_settings = {
		'DOWNLOAD_DELAY': 2, # 2 seconds of delay
        'RANDOMIZE_DOWNLOAD_DELAY': True
		}
    
    
    def start_requests(self):
        # start from the 1st page
        for page in range(1, 3):
            yield scrapy.Request(f'https://jobs.steward.org/joblist?page_size=50&page_number={page}&sort_by=headline&sort_order=ASC')
    
    
    def parse(self, response):
        BASE_URL = "https://jobs.steward.org"
        url_list = response.css('.item-title a::attr(href)').getall()
        
        # iterate by job posting`s url
        for url in url_list:
            next_url = BASE_URL + url
            
            yield scrapy.Request(next_url, callback=self.parse_job)
    
    
    def parse_job(self, response):
        """
        Get job postings details as dict
        """   
        job_id = response.css('p.job-ref::text').getall()[1]
        title = response.css('.job-title::text').get()
        location = response.css('.location-info::text').get()
        date_posted = response.css('#posted-date::text').get()
        job_type = response.css('.job-type::text').get()
        description = response.css('.job-description-content ::text').getall()[7:]
            
        yield {
            "id": job_id,
            "title": title,
            "location": location,
            "job_type": job_type,
            "date_posted": date_posted,
            "date_scraped": self.today,
            "description": description,
            "url": response.url
            }