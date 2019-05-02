import datetime
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.remitrate.com/best-exchange-rates/compare-USD-to-PHP',
    ]

    def parse(self, response):

        BOX_SELECTOR = '.box.box-solid.bg-gray'
        for box in response.css(BOX_SELECTOR):


            # Not really useful to add documentation, need to read through website HTML
            NAME_SELECTOR = './/div[@class="small-box bg-gray"]/a/text()'
            TIME_UNITS_SELECTOR = './/span[1]/text()'
            TIME_SELECTOR = './/div[@class="rateNumber"]/span[not(@*)]/text()'
            LOCKED_IN_RATE_SELECTOR = './/div[@class="col-lg-2"][2]' \
                                      '//span[@class="currRate"]/text()'
            FEES_SELECTOR = './/div[@class="col-lg-9"]' \
                            '//div[@class="col-lg-3"]' \
                            '/div/span/text()[position() = last()]'
            TOTAL_PHP_AMT_SELECTOR = './/div[@class="col-lg-9"]' \
                                     '//div[@class="col-lg-3"]' \
                                     '//div[@class="rateNumber"]' \
                                     '/text()[2]'
            EFFECTIVE_RATE_SELECTOR = './/div[@class="col-lg-9"]' \
                                      '//div[@class="rateNumber text-light-blue"]' \
                                      '/text()[2]'                                          
                                    
            yield {
                'datetime accessed': str(datetime.datetime.now()),
                'company name': box.xpath(NAME_SELECTOR).get().strip(),
                'time units': box.xpath(TIME_UNITS_SELECTOR).get().strip(),
                'time': box.xpath(TIME_SELECTOR).get().strip(),
                'locked-in rate': box.xpath(LOCKED_IN_RATE_SELECTOR).get().strip(),
                'fees string': box.xpath(FEES_SELECTOR).get().strip(),
                'total PHP amt': box.xpath(TOTAL_PHP_AMT_SELECTOR).get().strip(),
                'effective rate': box.xpath(EFFECTIVE_RATE_SELECTOR).get().strip(),
            }