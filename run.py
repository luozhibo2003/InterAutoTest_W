"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: run.py
    @time: 2019-10-19 22:47
    @desc: 
"""

import os
import pytest

from common import Base
from config import Conf

if __name__ == '__main__':
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"
    pytest.main(["-s", "--alluredir", report_path])
    # Base.send_mail()
