"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: Test_Mall.py
    @time: 2019-10-22 12:17
    @desc: 
"""

import requests


def login():
    url = "http://211.103.136.242:8064/authorizations/"
    data = {"username": "python", "password": "12345678"}
    res = requests.post(url, json=data)
    print(res.json())


def info():
    # 1、参数
    url = "http://211.103.136.242:8064/user/"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InB5dGhvbiIsImV4cCI6MTU3MTgwNDM0OX0.thlFjSd2SYVuqEBp49NJRQSn_z2RW3CQO0N9Y15rjfA"
    headers = {
        'Authorization': 'JWT ' + token
    }
    res = requests.get(url, headers=headers)
    print(res.json())


def goods_list():
    url = "http://211.103.136.242:8064/categories/115/skus/"
    data = {
        "page": "1",
        "page_size": "10",
        "ordering": "create_time"
    }
    # 2、请求
    r = requests.get(url, json=data)
    # 3、结果
    print(r.json())


def cart():
    url = "http://211.103.136.242:8064/cart/"
    data = {"sku_id": "3", "count": "1", "selected": "true"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InB5dGhvbiIsImV4cCI6MTU3MTgwNDM0OX0.thlFjSd2SYVuqEBp49NJRQSn_z2RW3CQO0N9Y15rjfA"
    headers = {
        'Authorization': 'JWT ' + token
    }

    r = requests.post(url, json=data, headers=headers)
    print(r.json())


def order():
    url = "http://211.103.136.242:8064/orders/"
    data = {"address": "1", "pay_method": "1"}
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InB5dGhvbiIsImV4cCI6MTU3MTgwNDM0OX0.thlFjSd2SYVuqEBp49NJRQSn_z2RW3CQO0N9Y15rjfA"
    headers = {
        'Authorization': 'JWT ' + token
    }

    r = requests.post(url, json=data, headers=headers)

    print(r.json())


if __name__ == '__main__':
    # login()
    # info()
    # goods_list()
    # cart()
    order()
