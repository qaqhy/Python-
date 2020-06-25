# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhaopingSpider(CrawlSpider):
    name = 'zhaoping'
    allowed_domains = ['yingjiesheng.com']
    start_urls = ['http://www.yingjiesheng.com/commend-fulltime-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/job-\d{3}-\d{3}-\d{3}\.html'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'/commend-fulltime-\d+\.html'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['公司名称'] = ''.join(response.xpath('//div[@class]/h1/text()').get().split())
        ds = response.xpath('//div[@class]/ol/li/u/text()').getall()
        if ds:
            item['发布时间'] = ds[0]
            item['工作地点'] = ds[1]
            item['职位类型'] = ds[2]
        print(item)
        return item
