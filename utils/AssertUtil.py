"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: AssertUtil.py
    @time: 2019-10-22 18:22
    @desc: 
"""
import json

from utils.LogUtil import my_log


class AssertUtil:

    def __init__(self):
        self.log = my_log("AssertUtil")

    # 3、code相等
    def assert_code(self, code, expected_code):
        try:
            assert int(code) == int(expected_code)
        except:
            self.log.error("code error,code is %s,expected_code is %s" % (code, expected_code))
            raise

    # 4、body相等
    def assert_body(self,body,expected_body):
        try:
            assert body == expected_body
            return True
        except:
            self.log.error("body error,body is %s,expected_body is %s" % (body, expected_body))
            raise

    # 5、body包含
    def assert_in_body(self,body,expected_body):
        try:
            body = json.dumps(body)
            print(body)
            assert expected_body in body
            return True
        except:
            self.log.error("不包含或者body是错误，body is %s,expected_body is %s" % (body, expected_body))
            raise

