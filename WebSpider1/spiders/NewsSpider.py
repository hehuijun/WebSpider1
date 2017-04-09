#引入文件
import scrapy
#引入容器
from WebSpider1.NewsItems import NewsItems
class NewsSpider(scrapy.Item):
    #用于区别Spider
    name = 'NewsSpider'
    #允许访问的域名
    allowed_domains =['http://news.csi.com.cn']
    #爬取开始的地址
    start_urls = ['http://news.csi.com.cn/WJ008.html']
    #爬取方法
    def parse(self,response):
        #实例一个容器保存爬取的信息
        item = NewsItems()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 获取每个新闻的div
        for box in response.xpath('//div[@id="rpt_title"]'):

            #获取div中的新闻路径
            item['url'] = box.xpath('a/@href').extract()[0]
            #获取div中的新闻标题
            item['title'] = box.xpath('a/text()').extract().strip()
            #返回信息
            yield item
