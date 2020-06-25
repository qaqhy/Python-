# -*- coding: utf-8 -*-
import scrapy
import re


class RrSpider(scrapy.Spider):
    name = 'rr'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/974623567/newsfeed/photo']

    def start_requests(self):
        cookies = 'anonymid=kbp0f7uw-4m0oe6; depovince=CQ; _r01_=1; ' \
                  'taihe_bi_sdk_uid=f227e213ba37fd11a00b5b40237fd5c0; _de=4AE88CE1E14521CDE0538E02551DF692; ' \
                  'p=43d5c38cfa3568f1d6dec4c5d549e34b7; ap=974623567; ln_uact=18323019610; ' \
                  'ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; ' \
                  'jebecookies=354f26bd-5dab-4bf7-b189-183fed761d88|||||; JSESSIONID=abcDTKOCLRZ8PdA7wRzlx; ' \
                  'first_login_flag=1; t=1a30c676b115918ae9e31edb9e77a0507; ' \
                  'societyguester=1a30c676b115918ae9e31edb9e77a0507; id=974623567; xnsid=2652901c; ver=7.0; ' \
                  'loginfrom=null; taihe_bi_sdk_session=422f215880fc9fe2aa7dec0d06a1fde1; ' \
                  '_ga=GA1.2.1310317856.1592790405; _gid=GA1.2.716303228.1592790405 '

        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall("侯尧", response.body.decode()))
        yield scrapy.Request(
            'http://zhibo.renren.com/',
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        with open('./temp.html', 'w', encoding='utf-8') as w:
            w.write(response.body.decode())
        print(re.findall("侯尧", response.body.decode()))
