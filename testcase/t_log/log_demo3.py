"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: log_demo3.py
    @time: 2019-10-22 09:52
    @desc:

    优点：
    1.把日志保存到文件
    2.info的信息也打印出来

    缺点：
    1.对于不同的项目需要弄不同,不灵活
    2.一直往文件写入,不可控,不能打印
    3.参数全部固定不变的
"""

# 把日志保存到文件
# info的信息也打印出来
import logging

logging.basicConfig(filename='access.log',  # 指定日志文件保存的文件名，没有就生成access.log
                    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s:%(message)s',  # 指定日志的格式
                    level=10)  # 控制保存日志的最低等级

name = input('name>>>')
total_prize = input('total_prize>>>')

logging.info(f'{name}消费了{total_prize}')
logging.debug(f'{name}消费了{total_prize}')
logging.warning(f'{name}消费了{total_prize}')
logging.error(f'{name}消费了{total_prize}')
logging.critical(f'{name}消费了{total_prize}')

# 2019-10-22 09:56:57,513 - root - INFO - log_demo3:luobotou消费了300
# 2019-10-22 09:56:57,514 - root - DEBUG - log_demo3:luobotou消费了300
# 2019-10-22 09:56:57,514 - root - WARNING - log_demo3:luobotou消费了300
# 2019-10-22 09:56:57,514 - root - ERROR - log_demo3:luobotou消费了300
# 2019-10-22 09:56:57,514 - root - CRITICAL - log_demo3:luobotou消费了300
