# -*- coding: utf-8 -*-
import scrapy
import time
from tencent.items import TencentItem


class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['tencent.com']
    timestamp = int(time.time()*10**3)
    print(f'timestamp:{timestamp}')
    start_urls = [f'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={timestamp}'
                  f'&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=40001&attrId=&keyword=&'
                  f'pageIndex=1&pageSize=10&language=zh-cn&area=cn']
    'referer: https://careers.tencent.com/search.html?pcid=40001'

    def parse(self, response):
        items = TencentItem()
        items['sex'] = '男'
        items['name'] = '测试'
        print(items)
        print(response.meta)
