"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: pytest_class.py
    @time: 2019-10-22 12:03
    @desc: 
"""

"""
1、定义类
2、创建测试方法test开头
3、创建setup_class,teardown_class
4、运行查看结果

"""

import pytest


class TestClass:
    def setup_class(self):
        print("-----setup_class----")

    def teardown_class(self):
        print("-----teardown_class-----")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")


if __name__ == '__main__':
    pytest.main(["-s", "pytest_class.py"])
