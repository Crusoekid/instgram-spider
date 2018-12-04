import scrapy
import os
import urllib
import requests
from hashlib import md5
from ..items import InstagramItem
from ..spiders.constantant import *
from .jsonutil import jsonHandler
from .fileutil import fileHandler

class dataHandler:
    def savedata(self,edges):
        for edge in edges:
            it = InstagramItem()
            it['name_'] = edge['node']['username']
            it['id_'] = edge['node']['id']
            it['portrait_url_'] = edge['node']['profile_pic_url']
            yield it

    def downloadPortrait(self,url):   
        fileHandler().existportraitfolder()
        response = jsonHandler().get_reponse(url)
        content = response.content
        filetype = url[-4:]
        if filetype !='.jpg' and filetype!='.png':
            filetype = '.jpg'
        img_name = SAVE_PORTRAIT_PATH + md5(content).hexdigest() + filetype
        with open(img_name, 'wb') as file:
            file.write(content)
            file.flush()
        file.close()
        print('下载完成')

    def downloadPhoto(self,url,user):
        path = fileHandler().existuserfolder(user)
        response = jsonHandler().get_reponse(url)
        content = response.content
        filetype = url[-4:]
        if filetype !='.jpg' and filetype!='.png':
            filetype = '.jpg'
        img_name = path + md5(content).hexdigest() + filetype
        with open(img_name, 'wb') as file:
            file.write(content)
            file.flush()
        file.close()
        print('下载完成')