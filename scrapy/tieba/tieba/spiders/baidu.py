# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import re
from lxml import etree


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%99%BE%E5%BA%A6&ie=utf-8&tab=good&cid=0&pn=0']

    def parse(self, response):
        a_list = response.xpath('//code[@id="pagelet_html_frs-list/pagelet/thread_list"]/text()')
        items = []
        for a in a_list:
            title = a.xpath('./@title')
            href = a.xpath('./@href')
            url = None if href is None else urllib.parse.urljoin(response.url, href)
            items.append({'title': title, 'url': url})
        print(items)

