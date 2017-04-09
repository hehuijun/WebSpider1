#引入文件
import scrapy

class NewsSpider(scrapy.Item):
    #用于区别Spider
    name = 'NewsSpider'
