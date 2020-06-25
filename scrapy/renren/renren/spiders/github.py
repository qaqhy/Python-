# -*- coding: utf-8 -*-
import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').extract_first()
        timestamp = response.xpath('//input[@name="timestamp"]/@value').extract_first()
        timestamp_secret = response.xpath('//input[@name="timestamp_secret"]/@value').extract_first()
        post_data = {
            "commit": "Sign in",
            "authenticity_token": authenticity_token,
            "login": "username",
            "password": "password",
            "webauthn-support": "supported",
            "webauthn-iuvpaa-support": "unsupported",
            "timestamp": timestamp,
            "timestamp_secret": timestamp_secret
        }
        yield scrapy.FormRequest(
            "https://github.com/session",
            formdata=post_data,
            callback=self.after_login,
        )

    def after_login(self, response):
        with open("temp.html", 'w', encoding='utf-8') as w:
            w.write(response.body.decode())
        print(re.findall("houyao2910277944", response.body.decode()))

