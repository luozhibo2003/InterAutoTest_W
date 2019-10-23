"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: allure_demo.py
    @time: 2019-10-22 12:57
    @desc: 
"""

import pytest
import allure


@allure.feature("接口测试，这是一个一级标签")
class TestAllure:

    @allure.story("这是一个二级标标签：test1")
    @allure.title("测试用例标题1")
    @allure.description("执行测试用例1的结果是test2")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_1(self):
        print("test1")

    @allure.story("这是一个二级标标签：test3")
    @allure.title("测试用例标题2")
    @allure.description("执行测试用例1的结果是test2")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("test2")

    @allure.story("这是一个二级标标签：test3")
    @allure.title("测试用例标题3")
    @allure.description("执行测试用例1的结果是test3")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_3(self):
        print("test3")

    @pytest.mark.parametrize("case", ["动态测试用例1", "动态测试用例2"])
    def test_4(self, case):
        print(case)
        print("test4")
        allure.dynamic.title(case)
        allure.dynamic.story(case)


if __name__ == '__main__':
    pytest.main(["allure_demo.py"])
