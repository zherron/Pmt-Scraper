import schedule
import time
import csv

import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_quotes.spiders.quotes_spider import QuotesSpider

"""
Runs the scrapy spider. This function needs to be housed within the scrapy project
Spider (QuotesSpider) outputs to quotes.csv.
If errors, check quotes.log for debugging log
"""
def get_quotes():
    settings = get_project_settings()
    settings['FEED_FORMAT'] = 'csv'
    settings['FEED_URI'] = 'quotes.csv'
    settings['LOG_LEVEL'] = 'INFO'
    settings['LOG_FILE'] = 'quotes.log'

    process = CrawlerProcess(settings)
    process.crawl(QuotesSpider())
    process.start()

"""
Reads through quotes.csv and rewrites to quotes_cleaned.csv all the
data, but without duplicate headers (that scrapy necessarily outputs)
"""
def clean_quotes_csv():
    # Opens quotes.csv as read, opens quotes_cleaned as write
    with open('quotes.csv', 'r') as inp, \
    open('quotes_cleaned.csv', 'w') as out:
        writer = csv.writer(out)
        line_count = 0
        for row in csv.reader(inp):
            # If row doesn't have content of title row, and isn't the first row
            if row[0] != "datetime accessed" \
            or line_count == 0:
                writer.writerow(row)
                line_count += 1

def get_quotes_and_clean():
    get_quotes()
    clean_quotes_csv()


