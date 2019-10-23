"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: pytest_two.py
    @time: 2019-10-22 12:12
    @desc: 
"""
import pytest

"""
1、创建类和测试方法
2、创建数据
3、创建参数化
4、运行
"""


class TestDemo:
    data_list = [("xiaoming", "123355"), ("xiaohong", "334545")]

    @pytest.mark.parametrize(("name", "password"), data_list)
    def test_a(self, name, password):
        print("test_a")
        print(name, password)
        assert 1


if __name__ == "__main__":
    pytest.main(["-s", "pytest_two.py"])
