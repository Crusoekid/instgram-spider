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
    t_img_url = ''
    count = 0
    # start_urls = [
    #     'https://www.instagram.com/giuliogroebert/',
    # ]

    def start_requests(self):
        print('---------------start_requests----------------------')
        # while self.account == '':
        #     js_data = jsonHandler().get_json(REQUEST_SUGGEST_URL)
        #     self.account = js_data['data']['user']['edge_suggested_users']['edges'][1]['node']['user']['username']
        if self.account != '':
            url = BEGIN_URL.format(self.account) 
            yield Request(url,callback=self.parse_hd_pic)
        else:
            print('Enter ACCOUNT')

    def __init__(self):
        print('---------------init  downloader----------------------')
        self.Spide_num = int(input("How many?  "))
        self.account = input("Enter Account: ")
        self.count = 0
        fileHandler().existtestfolder()
        fileHandler().existphotofolder()
        
    def parse_hd_pic(self, response):
        print('---------------parse_hd_pic----------------------')
        t_img_url = ''
        self.getProfile(response)
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)

        edges = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
        page_info = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]['page_info']
        end_cursor = page_info['end_cursor']
        next_page = page_info['has_next_page']

        self.saveAndDownload(edges)
        
        while next_page:
            url = REQUEST_NEXT_PIC_URL.format(self.user_id, end_cursor)    
            js_data = jsonHandler().get_json(url)
            
            edges = js_data['data']['user']['edge_owner_to_timeline_media']['edges']
            end_cursor = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            next_page = js_data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
            if self.count >= self.Spide_num:
                break
            else:
                self.saveAndDownload(edges)
        fileHandler().writefile(t_img_url)

    def saveAndDownload(self,edges):
        for edge in edges:
            img_url = edge['node']['display_url']
            if img_url and self.count < self.Spide_num:   
                self.t_img_url = self.t_img_url + img_url + '\n'
                self.count+=1
                dataHandler().downloadPhoto(img_url,self.user_name)

    def getProfile(self , response):
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)
        owner_data = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["owner"]
        self.user_id = owner_data["id"]
        self.user_name = owner_data["username"]
        print(self.user_name)

