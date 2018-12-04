# -*- coding: utf-8 -*-
import scrapy
import os
import json
import requests
from .constantant import *
from ..utils.fileutil import fileHandler
from ..utils.jsonutil import jsonHandler
from ..utils.datautil import dataHandler
from ..items import InstagramItem
from scrapy.http.request import Request


class DownloadSpider(scrapy.Spider):
    name = 'downloader'
    user_id = ''
    user_name = ''
    Spide_num = 0
    account = ''
    count = 0
    start_urls = [
        'https://www.instagram.com/giuliogroebert/',
    ]

    def __init__(self):
        print('---------------init----------------------')
        self.count = 0
        fileHandler().existtestfolder()
        fileHandler().existphotofolder()

    def parse(self, response):
        print('=================' + response.url + '====================')
        self.getProfile(response)
        request = Request(response.url, callback=self.parse_hd_pic)
        yield request

    def parse_hd_pic(self, response):
        t_img_url = ""
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)
        imgs = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
        page_info = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]['page_info']
        end_cursor = page_info['end_cursor']
        next_page = page_info['has_next_page']
        for img in imgs:
            img_url = img['node']['display_url']
            if img_url:          
                t_img_url = t_img_url + img_url + '\n'
                dataHandler().downloadPhoto(img_url,self.user_name)
        
        # while next_page:
        #     url = REQUEST_NEXT_PIC_URL.format(self.user_id, end_cursor)    
        #     js_data = jsonHandler().get_json(url)
            
        #     infos = js_data['data']['user']['edge_owner_to_timeline_media']['edges']
        #     end_cursor = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        #     next_page = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
        #     for info in infos:
        #         if info['node']['is_video']:
        #             video_url = info['node']['video_url']
        #             if video_url:
        #                 t_img_url = t_img_url + video_url + '\n'
        #         else:
        #             if info['node']['display_url']:
        #                 display_url = info['node']['display_url']
        #                 t_img_url = t_img_url + display_url + '\n' 
        fileHandler().writefile(t_img_url)

    def getProfile(self , response):
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)
        owner_data = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["owner"]
        self.user_id = owner_data["id"]
        self.user_name = owner_data["username"]

