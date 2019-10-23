"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: pytest_func.py
    @time: 2019-10-22 12:06
    @desc: 
"""

"""
1、定义类
2、创建测试方法test开头
3、创建setup,teardown
4、运行查看结果

"""

import pytest


class TestFunc:
    def setup(self):
        print("-----setup-----")

    def teardown(self):
        print("------teardown------")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")


# 4、运行查看结果
if __name__ == "__main__":
    pytest.main(["-s", "pytest_func.py"])
