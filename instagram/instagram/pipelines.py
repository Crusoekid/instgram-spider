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

# 输出一个json数组
class InstagramPipeline(object):
    def __init__(self):
        # 使用codecs模块的打开方式，可以指定编码打开，避免很多编码问题
        dispatcher.connect(self.spider_closed,signals.spider_closed)
        self.file = codecs.open("people.json","w",encoding="utf-8")
        self.file.write("[\n")

    def process_item(self,item,spider):
        # if item['id'] in self.:
        #     raise DropItem("Duplicate item found: %s" % item)
        # else:
        #     self.ids_seen.add(item['id'])
        #     return item
        lines = json.dumps(dict(item) , ensure_ascii=False) + ","+ "\n"
        self.file.write(lines)

        #注意别忘返回Item给下一个管道
        return item

    def spider_closed(self,spider):
        self.file.write("]")
        self.file.close()

# 输出一个json数组->模板
class InstagramPipelineList(object):
    def __init__(self):
        dispatcher.connect(self.spider_closed,signals.spider_closed)
        self.file = open('test.json', 'wb')
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item

    def spider_closed(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

# 默认的管道
class DefaultPipeline(object):
    def process_item(self,item,spider):
        return item

# class ArticleImagePipeline(ImagesPipeline):
#     '''添加图片的目录'''
#     def item_completed(self, results, item, info):  #重载
#         try:
#             if "front_image_url" in item:
#                 for ok, value in results:
#                     image_file_path = value["path"]
#                 item["front_image_path"] = image_file_path
#             return item
#         except Exception as e:
#             print(e)
#             item["front_image_path"] = 'no_use'
#             return item