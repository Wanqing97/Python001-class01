# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem


class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        print(response.url)
        titles = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for i in titles:
        # 在Python中应该这样写
	    # for i in title_list:
            # 在items.py定义
            item = MaoyanmovieItem()
            title = i.xpath('./a/text()')
            link =  i.xpath('./a/@href')
            item['title'] = title.extract_first().strip()
            item['link'] = 'https://' + self.allowed_domains[0] + link.extract_first().strip()
            yield scrapy.Request(url=item['link'],meta={'item': item},callback=self.parse2)

    def parse2(self,response):
        item = response.meta['item']
        infos = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        for j in infos:
            category = j.xpath('./ul/li/a/text()').extract()
            time = j.xpath('./ul/li[last()]/text()').extract_first().strip()
            item['category'] = category
            item['time'] = time

        yield item

