import schedule
import time

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_quotes.spiders.quotes_spider import QuotesSpider


def get_quotes():
    settings = get_project_settings()
    settings['FEED_FORMAT'] = 'csv'
    settings['FEED_URI'] = 'quotes.csv'
    settings['LOG_LEVEL'] = 'INFO'
    settings['LOG_FILE'] = 'quotes.log'

    process = CrawlerProcess(settings)
    process.crawl(QuotesSpider())
    process.start()

schedule.every().day.at("09:30").do(get_quotes)

while True:
    schedule.run_pending()
    time.sleep(60)
