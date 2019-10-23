"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: t_requests.py
    @time: 2019-10-20 08:14
    @desc: 
"""

import requests

r = requests.get("http://www.baidu.com")

print(r.status_code)  # 响应状态
print(r.content)  # 以字节方式返回响应体，会自动解码gzip和deflate压缩
print(r.headers)  # 以字典对象存储服务器响应，若健不存在则返回None
print(r.url)  # 获取url
# print(r.json()) # Request内置中的json
print(r.encoding)  # 编码格式
print(r.cookies)  # 获取cookie
print(r.raw)  # 返回原始响应体
print(r.text)  # 字符串方式的响应体
print(r.raise_for_status())  # 失败请求（非200响应）返回异常
