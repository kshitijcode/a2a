
import argparse
import scrapy
from scrapy.crawler import CrawlerProcess
from tabulate import tabulate
import logging


class GithubSpider(scrapy.Spider):
    service = 'default'
    name = 'github'
    start_urls = ['https://github.com/MicrosoftDocs/architecture-center/blob/master/docs/aws-professional/services.md']

    def parse(self, response):
        tables = response.css('table')
        for table in tables:
            rows = table.xpath('//tr//td')
            for index, row in enumerate(rows):
                keywords = row.xpath('a//node()').extract()
                url = row.xpath('a/@href').extract()
                if self.service.lower() in (keyword.lower() for keyword in keywords):
                    matched_service = rows[index + 1].xpath('a//node()').extract() if rows[index + 1].xpath(
                        'a//node()').extract() else rows[index - 1].xpath('a//node()').extract()
                    matched_url = rows[index + 1].xpath('a/@href').extract() if rows[index + 1].xpath(
                        'a/@href').extract() else rows[index - 1].xpath('a/@href').extract()

                    print(tabulate([[keywords, url, matched_service, matched_url]], headers=['SERVICE', 'URL',
                                                                                             'CORRESPONDING SERVICES',
                                                                                             'CORRESPONDING URLS']))
                    return


def runner():
    parser = argparse.ArgumentParser(description='Enter the values to fetch the corresponding service')
    parser.add_argument('service', type=str, help='Enter the name of service')
    args = parser.parse_args()

    GithubSpider.service = args.service
    logging.getLogger('scrapy').propagate = False

    process = CrawlerProcess()
    process.crawl(GithubSpider)
    process.start()
