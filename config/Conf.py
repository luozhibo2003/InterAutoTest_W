# -*- coding:utf-8 -*-
"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: Conf.py
    @time: 2019-10-22 11:16
    @desc: 
"""

import os
from utils.YamlUtil import YamlReader

# 获取项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# 定义config目录路径
_config_path = BASE_DIR + os.sep + "config"

# 定义data目录的路径
_data_path = BASE_DIR + os.sep + "data"

# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"

# 定义report目录的路径
_report_path = BASE_DIR + os.sep + "report"

# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + "conf.yml"

# 定义db_conf.yml路径
_db_config_file = _config_path + os.sep + "db_conf.yml"


def get_report_path():
    return _report_path


def get_data_path():
    return _data_path


def get_db_config_file():
    return _db_config_file


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def get_log_path():
    return _log_path


class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    # 定义方法获取需要信息
    def get_excel_file(self):
        """
        获取测试用例excel名称
        :return:
        """
        return self.config["BASE"]["test"]["case_file"]

    def get_excel_sheet(self):
        """
        获取测试用例sheet名称
        :return:
        """
        return self.config["BASE"]["test"]["case_sheet"]

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        获取日志级别
        :return:
        """
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """
        获取文件扩展名
        :return:
        """
        return self.config["BASE"]["log_extension"]

    def get_db_conf_info(self, db_alias):
        """
        根据db_alias获取该名称下的数据库信息
        :param db_alias:
        :return:
        """
        return self.db_config[db_alias]

    def get_email_info(self):
        """
        获取邮件配置相关信息
        :return:
        """
        return self.config["email"]


if __name__ == "__main__":
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info("db_1"))
    # print(conf_read.get_db_conf_info("db_2"))
    # print(conf_read.get_db_conf_info("db_3"))
    # 1、初始化数据库信息，Base.py init_db
    # 2、接口用例返回结果内容进数据库验证
    # print(conf_read.get_excel_file())
    # print(conf_read.get_excel_sheet())
    print(conf_read.get_email_info())
