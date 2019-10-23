"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: pytest_demo.py
    @time: 2019-10-22 11:44
    @desc: 
"""

# 1、创建简单测试方法
import pytest

"""
1、创建普通方法
2、使用pytest断言的方法
"""


# 普通方法
def func(x):
    return x + 1


# 断言方法
def test_a():
    print("------test_a-----")
    assert func(3) == 5  # 断言失败


def test_b():
    print("------test_b-----")
    assert 1


@pytest.mark.flaky(reruns=3, reruns_delay=2)
def test_c():
    print("------test_c-----")
    assert func(3) == 5


# 2、pytest运行
"""
1、Pycharm代码直接执行
2、命令行执行
"""

if __name__ == '__main__':
    pytest.main(["-s", "pytest_demo.py"])
