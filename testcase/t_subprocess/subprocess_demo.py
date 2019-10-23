"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: subprocess_demo.py
    @time: 2019-10-22 17:53
    @desc: 
"""

import subprocess

res = subprocess.call(["ls","-s"])

print(res)

subprocess.call("ls -l",shell=True)