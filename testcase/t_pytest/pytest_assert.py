"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: pytest_assert.py
    @time: 2019-10-22 11:55
    @desc: 
"""

import pytest


def test_1():
    a = True
    assert a


def test_2():
    a = True
    assert not a


def test_3():
    a = "hello"
    b = "hello world"
    assert a in b


def test_4():
    a = b = "hello"
    assert a == b


def test_5():
    a = "hello"
    b = "hello world"
    assert a != b


if __name__ == '__main__':
    pytest.main(["pytest_assert.py"])
