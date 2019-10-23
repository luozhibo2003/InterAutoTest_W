# -*- coding:utf-8 -*-
"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: RequestsUtil.py
    @time: 2019-10-22 12:26
    @desc: 
"""

import requests


def requests_get(url, headers):
    r = requests.get(url, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 内容存到字典中
    res = dict()
    res["code"] = code
    res["body"] = body

    return res


def request_post(url, json=None, headers=None):
    r = requests.post(url, json=json, headers=headers)
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 内容存到字典中
    res = dict()
    res["code"] = code
    res["body"] = body

    return res


# 将get和post方法进行重构，
class Request:
    def __init__(self):
        # self.log = my_log('Requests')
        pass

    def requests_api(self, url, data=None, json=None, headers=None, cookies=None, method="get"):
        if method == "get":
            r = requests.get(url, data=data, json=json, headers=headers, cookies=cookies)
        elif method == "post":
            r = requests.post(url, data=data, json=json, headers=headers, cookies=cookies)

        code = r.status_code
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 内容存到字典中
        res = dict()
        res["code"] = code
        res["body"] = body

        return res

    # 重构get / post方法
    def get(self, url, **kwargs):
        return self.requests_api(url, method="get", **kwargs)

    def post(self, url, **kwargs):
        return self.requests_api(url, method="post", **kwargs)
