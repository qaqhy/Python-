# -*- coding: utf-8 -*-
import scrapy
from suning.items import SuningItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['list.suning.com', 'product.suning.com']
    start_urls = ['https://list.suning.com/0-502319-0.html?safp=d488778a.homepage1.99345513004.50&safc=cate.0.0&safpn'
                  '=10001']

    def parse(self, response):
        # with open('./temp.html', 'w', encoding='utf-8') as w:
        #     w.write(response.text)
        divs = response.xpath('//div[@class="title-selling-point"]/a[@sa-data]')
        for div in divs:
            # print(div.get())
            item = SuningItem()
            item['title'] = ''.join(div.xpath('./@title').getall())
            item['href'] = div.xpath('./@href').extract_first()
            if item['href'] is not None:
                item['href'] = 'http:' + item['href']
                yield scrapy.Request(
                    item['href'],
                    callback=self.parser,
                    meta={'item': item})

    def parser(self, response):
        item = response.meta['item']
        item['author'] = ''.join(response.xpath('//li[@class="pb-item"]/text()').get().split())
        yield item

