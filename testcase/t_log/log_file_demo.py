"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: log_file_demo.py
    @time: 2019-10-20 17:28
    @desc: 
"""

import logging

# 输出控制台
# 1、设置logger名称
logger = logging.getLogger("log_file_demo")
# 2、设置log级别
logger.setLevel(logging.INFO)
# 3、创建handler
fh_stream = logging.StreamHandler()
# 写入文件
fh_file = logging.FileHandler("./test.log")
# 4、 设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.WARNING)
# 5、定义输出格式
formater = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
fh_stream.setFormatter(formater)
fh_file.setFormatter(formater)
# 6、添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
# 7、 运行输出
logger.info("this is a info")
logger.info("this is a debug")
logger.info("this is a warning")
