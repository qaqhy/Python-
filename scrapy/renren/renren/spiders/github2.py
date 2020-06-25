# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github2'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                "login": "username",
                "password": "password",
            },
            callback = self.after_login,
        )

    def after_login(self, response):
        with open("temp.html", 'w', encoding='utf-8') as w:
            w.write(response.body.decode())
        print(re.findall("houyao2910277944", response.body.decode()))

