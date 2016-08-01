#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://news.baidu.com/']
    def parse(self, response):
        for item in response.css('.hotnews ul li strong a'):
            yield {
                'title':item.xpath('text()').extract()[0],
                'url':item.xpath('@href').extract()[0]
            }
            # title = item.xpath('text()').extract()[0].decode("unicode-escape")
            # link = item.xpath('@href').extract()[0]
            # print title + " " + link + "\n"
            # full_url = response.urljoin(href.extract())
            # yield scrapy.Request(full_url, callback=self.parse_question)
    # def parse_question(self, response):
    #     yield {
    #     'title': response.css('h1 a::text').extract_first(),
    #     'votes': response.css('.question .vote-count-post::text').extract_first(),
    #     'body': response.css('.question .post-tex).extract_first(),
    #     'tags': response.css('.question .post-tag::text').extract(),
    #     'link': response.url,
    #     }
