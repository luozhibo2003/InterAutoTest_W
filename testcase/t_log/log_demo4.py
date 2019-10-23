"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: log_demo4.py
    @time: 2019-10-22 09:58
    @desc:
"""

import logging

# 1. logger 你是哪个版本日志  定义日志名称getlogger
logger = logging.getLogger('bank')

# 2.filter 不用管

# 3.handler 是保存在文件中，还是打印到屏幕中
t1 = logging.FileHandler('t1.log')
t2 = logging.FileHandler('t2.log')
sm = logging.StreamHandler()  # 往屏幕中打印

# 4.formater，控制日志格式
f1 = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s -  %(module)s:%(message)s',
                       datefmt='%Y-%m-%d %H:%M:%S %p', )
f2 = logging.Formatter('%(levelname)s - %(asctime)s : %(message)s',
                       datefmt='%Y-%m-%d %H:%M:%S %p', )
f3 = logging.Formatter('%(name)s - %(levelname)s - %(message)s', )

# 5. formater 绑定到handler里面去
t1.setFormatter(f1)
t2.setFormatter(f2)
sm.setFormatter(f3)

# 6. handler绑定到logger里面去
logger.addHandler(t1)
logger.addHandler(t2)
logger.addHandler(sm)

# 7.设置打印级别
logger.setLevel(10)  # 控制着全部,先走全部,再走单个的,如果不设置,默认30,必须得设置
t1.setLevel(20)
t1.setLevel(30)
t1.setLevel(40)

# 8.测试
logger.info('123')
logger.debug('123')
logger.warning('123')
logger.error('123')
logger.critical('123')
