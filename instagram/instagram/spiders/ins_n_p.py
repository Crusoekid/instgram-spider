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

class n_p_Spider(scrapy.Spider):
    name = 'ins_simple'
    user_id = ''
    user_name = ''
    Spide_num = 0
    account = ''
    count = 0
    # start_urls = [
    #     'https://www.instagram.com/giuliogroebert/',
    # ]

    def start_requests(self):
        print('---------------start_requests----------------------')
        while self.account == '':
            js_data = jsonHandler().get_json(REQUEST_SUGGEST_URL)
            self.account = js_data['data']['user']['edge_suggested_users']['edges'][1]['node']['user']['username']
        url = BEGIN_URL.format(self.account) 
        yield Request(url,callback=self.parse)
        

    def __init__(self):
        print('---------------init----------------------')
        self.Spide_num = int(input("How many?  "))
        self.account = input("Enter Account: ")
        self.count = 0
        # fileHandler().existfolder()    

    def parse(self, response):
        print('=================' + response.url + '====================')
        self.getProfile(response)
        url = REQUEST_FOLLOWERS_URL.format(self.user_id) 
        for i in self.parse_followers(url):
            yield i

    def parse_portrait(self, response):
        js = response.selector.xpath('//meta[@property="og:image"]/@content').extract()
        print('portrait=====>' + js)

    def parse_followers(self,url):
        print('---------------parse_followers----------------------')
        js_data = jsonHandler().get_json(url)
        edges = js_data['data']['user']['edge_followed_by']['edges']
        end_cursor = js_data['data']['user']['edge_followed_by']['page_info']['end_cursor']
        next_page = js_data['data']['user']['edge_followed_by']['page_info']['has_next_page']

        for edge in edges:
            self.count+=1
            if self.count > self.Spide_num:
                break
            it = InstagramItem()
            href = edge['node']['profile_pic_url']
            name = edge['node']['username']
            it['name_'] = name
            it['id_'] = edge['node']['id']
            it['portrait_url_'] = href
            yield it

        while next_page:
            if self.count > self.Spide_num:
                break
            url_next = REQUEST_NEXT_FOLLOWERS_URL.format(self.user_id,end_cursor)
            js_data = jsonHandler().get_json(url_next)

            edges = js_data['data']['user']['edge_followed_by']['edges']
            end_cursor = js_data['data']['user']['edge_followed_by']['page_info']['end_cursor']
            next_page = js_data['data']['user']['edge_followed_by']['page_info']['has_next_page']     

            for edge in edges:
                self.count+=1
                if self.count > self.Spide_num:
                    break
                it = InstagramItem()
                href = edge['node']['profile_pic_url']
                name = edge['node']['username']
                it['name_'] = name
                it['id_'] = edge['node']['id']
                it['portrait_url_'] = href
                yield it  

        if next_page == False and self.count < self.Spide_num:
            url = BEGIN_URL.format(name)
            yield scrapy.Request(url,callback=self.parse)
       
        print('---------------parse_followers Over----------------------')

    def parse_work_pic(self, response):
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
                dataHandler().downloadPortrait(img_url)
                # item = InstagramItem()
                # item['img_url_'] = img_url
                # yield item
        
        while next_page:
            url = REQUEST_NEXT_PIC_URL.format(self.user_id, end_cursor)    
            js_data = jsonHandler().get_json(url)
            
            infos = js_data['data']['user']['edge_owner_to_timeline_media']['edges']
            end_cursor = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            next_page = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
            for info in infos:
                if info['node']['is_video']:
                    video_url = info['node']['video_url']
                    if video_url:
                        t_img_url = t_img_url + video_url + '\n'
                else:
                    if info['node']['display_url']:
                        display_url = info['node']['display_url']
                        t_img_url = t_img_url + display_url + '\n' 
        fileHandler().writefile(t_img_url)
    

    def getProfile(self , response):
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)
        owner_data = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["owner"]
        self.user_id = owner_data["id"]
        self.user_name = owner_data["username"]

