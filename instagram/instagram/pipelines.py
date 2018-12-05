# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
from scrapy.exporters import JsonItemExporter
from scrapy.exceptions import DropItem
# from scrapy.pipelines.images import ImagesPipeline
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from .utils.google_cloud_datautil import gDataHandler

# 输出一个json
class InstagramPipeline(object):
    def __init__(self):
        pass

    def process_item(self,item,spider):
        # lines = json.dumps(dict(item) , ensure_ascii=False)
        gDataHandler().searchData(item)

        #注意别忘返回Item给下一个管道
        return item

    def spider_closed(self,spider):
        pass

# 输出一个json数组
class InstagramPipelineList(object):
    def __init__(self):
        # 使用codecs模块的打开方式，可以指定编码打开，避免很多编码问题
        dispatcher.connect(self.spider_closed,signals.spider_closed)
        self.file = codecs.open("people.json","w",encoding="utf-8")
        self.file.write("[\n")

    def process_item(self,item,spider):
        lines = json.dumps(dict(item) , ensure_ascii=False) + ","+ "\n"
        self.file.write(lines)

        #注意别忘返回Item给下一个管道
        return item

    def spider_closed(self,spider):
        self.file.write("]")
        self.file.close()


# 去重的ha
class InstagramPipelineSame(object):
    def __init__(self):
        # 使用codecs模块的打开方式，可以指定编码打开，避免很多编码问题
        dispatcher.connect(self.spider_closed,signals.spider_closed)
        self.file = codecs.open("people.json","w",encoding="utf-8")
        self.file.write("[\n")
        self.ids_seen = set()

    def process_item(self,item,spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
        lines = json.dumps(dict(item) , ensure_ascii=False) + ","+ "\n"
        self.file.write(lines)

    def spider_closed(self,spider):
        self.file.write("]")
        self.file.close()

# 默认的管道
class DefaultPipeline(object):
    def process_item(self,item,spider):
        return item
