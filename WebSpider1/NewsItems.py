#引入文件

import scrapy
class NewsItems(scrapy.Item):
    #新闻标题
    title = scrapy.Filed()
    #新闻URL
    url = scrapy.Filed()
