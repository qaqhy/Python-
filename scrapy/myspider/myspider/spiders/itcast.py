# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ajavaee']

    def parse(self, response):
        ds = response.xpath('//div[@class="li_txt"]/h3/text()').getall()
        logger.warning('日志文件')
        for d in ds:
            yield {'name': d}
        # return ds
