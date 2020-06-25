# -*- coding: utf-8 -*-
# 运行命令：scrapy crawl xicidaili
import scrapy


# 创建爬虫类  并且继承scarpy.Spider  最基础的类  另外几个类都是继承这个类
# scrapy有5个类，使用命令scarpy genspider -l可以查看
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'  # 爬虫名字必须唯一
    allowed_domains = ['xicidaili.com']  # 允许采集的域名
    start_urls = ['https://www.xicidaili.com/nn/']  # 开始采集的网站
    # start_urls = [f'https://www.xicidaili.com/nn/{page}' for page in range(1, 10)]  # 开始采集的网站

    # 解析响应数据
    def parse(self, response):
        # 提取数据
        # ip_ports = []
        selectors = response.xpath('//tr')
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()
            port = selector.xpath('./td[3]/text()').get()
            print(ip, port)
            # ip_ports.append([ip, port])
        # 翻页
        next_page = response.xpath('//a[@class="next_page"]/@href').get()
        if next_page:
            print(next_page)
            next_url = response.urljoin(next_page)  # 拼接url网址
            import time
            time.sleep(3)
            yield scrapy.Request(next_url, callback=self.parse, method='GET')
