# -*- coding: utf-8 -*-
import scrapy


class WenkuSpider(scrapy.Spider):
    name = 'wenku'
    allowed_domains = ['wenku.baidu.com']
    # start_urls = ['https://wenku.baidu.com/search?word=python&pn=0','https://wenku.baidu.com/search?word=python&pn=0','https://wenku.baidu.com/search?word=python&pn=0']
    start_urls = ['https://wenku.baidu.com/search?word=python&pn=0']
    p = 0

    def parse(self, response):
        dllist = response.selector.xpath("//dl")
        for dd in dllist:
            print(dd.css("p.fl a::attr('title')").extract_first())

        print("=" * 70)


        #设置多个回调
        self.p += 1
        if self.p < 10:
            next_url = 'https://wenku.baidu.com/search?word=python&pn='+str(self.p*10)
            url = response.urljoin(next_url) #构建绝对url地址（这里可省略）
            yield scrapy.Request(url=url,callable=self.parse)


