import json
import requests
import random
import time
import scrapy
from ..spiders.constantant import headers

class jsonHandler:
    def get_json(self,url):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                print('请求网页json错误, 错误状态码：', response.status_code)
        except Exception as e:
            print(e)
            time.sleep(60 + float(random.randint(1, 4000))/100)
            return self.get_json(url)

    def get_reponse(self,url):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response
            else:
                print('请求网页json错误, 错误状态码：', response.status_code)
        except Exception as e:
            print(e)
            time.sleep(60 + float(random.randint(1, 4000))/100)
            return self.get_reponse(url)