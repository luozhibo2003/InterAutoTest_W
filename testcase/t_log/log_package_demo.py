"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: log_package_demo.py
    @time: 2019-10-22 10:46
    @desc: 
"""

import time
import logging
from testcase.t_log import log_package

logger = logging.getLogger(__name__)  # 生成logger实例


def demo():
    logger.debug("start range... time:{}".format(time.time()))
    logger.info("中文测试开始...")
    for i in range(10):
        logger.debug("i:{}".format(i))
        time.sleep(0.2)
    else:
        logger.debug("over range... time:{}".format(time.time()))

    logger.debug("中文测试结束")


if __name__ == '__main__':
    log_package.load_my_logging_cfg()  # 在你程序文件的入口加载自定义logging配置
    demo()
