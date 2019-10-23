"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: yaml_demo.py
    @time: 2019-10-20 09:12
    @desc:
"""

import yaml


def readSingleDoc():
    # 打开文件
    with open("./data.yml", 'r', encoding='utf-8') as f:
        # 用yaml读取文件
        r = yaml.safe_load(f)
        print(r)


def readMultiDoc():
    with open("/Users/euming/Documents/PyCharm/InterAutoTest_W/data/testlogin.yml", 'r', encoding='utf-8') as f:
        # 用yaml读取文件
        r = yaml.safe_load_all(f)
        for i in r:
            print(i)


def readSingleDocByUtils():
    from utils.YamlUtil import YamlReader
    res = YamlReader("./data.yml").data()
    print(res)

def readMultiDocByUtils():
    from utils.YamlUtil import YamlReader
    res = YamlReader("./data.yml").data_all()


if __name__ == '__main__':
    # readSingleDoc()
    readMultiDoc()
    # readSingleDocByUtils()
