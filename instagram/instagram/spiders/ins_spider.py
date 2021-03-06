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

class InsSpider(scrapy.Spider):
    name = 'ins'
    user_id = ''
    user_name = ''
    Spide_num = 0
    account = ''
    count = 0

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

        if len(edges) == 0:
            return
        for edge in edges:
            if self.count >= self.Spide_num:
                break
            self.count+=1
            name = edge['node']['username']
            url = BEGIN_URL.format(name) 
            yield Request(url,callback=self.parse_profile)

        while next_page and self.count < self.Spide_num:
            url_next = REQUEST_NEXT_FOLLOWERS_URL.format(self.user_id,end_cursor)
            js_data = jsonHandler().get_json(url_next)

            edges = js_data['data']['user']['edge_followed_by']['edges']
            end_cursor = js_data['data']['user']['edge_followed_by']['page_info']['end_cursor']
            next_page = js_data['data']['user']['edge_followed_by']['page_info']['has_next_page']     

            for edge in edges:
                
                if self.count >= self.Spide_num:
                    break
                self.count+=1
                name = edge['node']['username']
                url = BEGIN_URL.format(name) 
                yield Request(url,callback=self.parse_profile) 

        if next_page == False and self.count < self.Spide_num:
            url = BEGIN_URL.format(name)
            yield scrapy.Request(url,callback=self.parse)
       
        print('---------------parse_followers Over----------------------')

    def parse_profile(self, response):
        print('---------------parse_profile ----------------------')
        t_img_url = ""
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)
        edges = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]
        for edge in edges:
            img_url = edge['node']["thumbnail_resources"][0]["src"]
            if img_url:          
                t_img_url = img_url
                break
        item = InstagramItem()
        item['name_'] = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["username"]
        item['id_'] = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["id"]
        profile_pic = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["profile_pic_url"]
        if profile_pic:
            item['portrait_url_'] = profile_pic
        else:
            item['portrait_url_'] = ''
        item['img_url_'] = t_img_url
        yield item
    

    def getProfile(self , response):
        js = response.selector.xpath('//script[contains(., "window._sharedData")]/text()').extract()
        js = js[0].replace("window._sharedData = ", "")
        jscleaned = js[:-1]
        js_data = json.loads(jscleaned)
        owner_data = js_data["entry_data"]["ProfilePage"][0]["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"][0]["node"]["owner"]
        self.user_id = owner_data["id"]
        self.user_name = owner_data["username"]

