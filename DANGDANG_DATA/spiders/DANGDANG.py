# -*- coding: utf-8 -*-
import scrapy
from  DANGDANG_DATA.items import DangdangDataItem


class DangdangSpider(scrapy.Spider):
    name = 'DANGDANG'
    allowed_domains = ['http://search.dangdang.com/']
    start_urls = ['http://search.dangdang.com/?key=%CA%D6%BB%FA&act=input&sort_type=sort_sale_amt_desc&page_index=1']

    def parse(self, response):

        for each in response.xpath("//div[@id='search_nature_rg']/ul[@id='component_59']/li"):
            print('1')
            item=DangdangDataItem()
            item['title']=each.xpath("./a/@title").extract_first()
            item['comment']=each.xpath("./p[@class='star']/a[@dd_name='单品评论']/text()").extract()[0][0:-3]
            print(item['comment'])

            yield item

        next_page = response.xpath("//ul[@name='Fy']/li[@class='next']/a/@href").extract_first()

        n=str(next_page)[-1]
        print(n)
        if (next_page is not None and int(n)<=8):
            n=int(n)+1
            next_page = "http://search.dangdang.com" + str(next_page)
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
        else:
            return
