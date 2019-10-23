"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: log_demo.py
    @time: 2019-10-20 17:16
    @desc: 
"""

# 1、导入Logging包
import logging

# 2、设置配置信息
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# 3、定义日志名称getlogger
logger = logging.getLogger('log_name')
# 4、info、debug
logger.info('info')
logger.debug('debug')
logger.warning('warning')
