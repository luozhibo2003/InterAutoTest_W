"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: log_demo2.py
    @time: 2019-10-22 09:48
    @desc: 
"""

import logging

name = input('name>>>')
total_prize = input('total_prize>>>')

logging.info(f'{name}消费了{total_prize}')
logging.debug(f'{name}消费了{total_prize}')
logging.warning(f'{name}消费了{total_prize}')
logging.error(f'{name}消费了{total_prize}')
logging.critical(f'{name}消费了{total_prize}')

# 默认只打印30级别以上，信息只在内存中打印出来，关闭就消失。
# name>>>luobo
# total_prize>>>300
# WARNING:root:luobo消费了300
# ERROR:root:luobo消费了300
# CRITICAL:root:luobo消费了300
