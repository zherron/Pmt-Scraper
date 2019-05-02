import schedule
import time
import csv

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

def clean_quotes_csv():
    with open('quotes.csv', 'r') as inp, \
    open('quotes_cleaned.csv', 'w') as out:
        writer = csv.writer(out)
        line_count = 0
        for row in csv.reader(inp):
            if row[0] != "datetime accessed" \
            or line_count == 0:
                writer.writerow(row)
                line_count += 1

def get_quotes_and_clean():
    get_quotes()
    clean_quotes_csv()

schedule.every().day.at("10:00").do(get_quotes_and_clean)

while True:
    schedule.run_pending()
    time.sleep(60)