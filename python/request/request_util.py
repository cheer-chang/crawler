# coding=utf8

import requests


class RequestUtil:
    # 请求连接返回response
    def __init__(self):
        pass

    @staticmethod
    def get(url):
        if url is None:
            return None
        # 伪装成一个浏览器
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        # 请求内容
        response = requests.get(url,
                                headers=headers,
                                params=None)
        response.encoding = "UTF-8"
        return response
