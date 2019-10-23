"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: ExcelData.py
    @time: 2019-10-23 07:47
    @desc: 
"""
from common.ExcelConfig import DataConfig
from utils.ExcelUtil import ExcelReader


class Data:
    def __init__(self,testcase_file,sheet_name):
        # 1、使用excel工具类，获取结果list
        # self.reader = ExcelReader("../data/testdata.xlsx","美多商城接口测试")
        self.reader = ExcelReader(testcase_file,sheet_name)
        print(self.reader.data())

    # 2、列是否运行内容，y
    def get_run_data(self):
        """
        根据使用运行列==y，获取执行测试用例
        :return:
        """
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                print(line)
                # 保存要执行的结果，放到新的列表
                run_list.append(line)
        print(run_list)
        return run_list

    def get_case_list(self):
        """
        获取全部测试用例
        :return:
        """
        run_list = [line for line in self.reader.data()]
        return run_list

    def get_case_pre(self,pre):
        # 获取全部测试用例
        # list判断，执行，获取
        """
        根据前置条件，从全部测试用例获取到测试用例
        :param pre:
        :return:
        """
        run_list = self.get_case_list()
        for line in run_list:
            if pre in dict(line).values():
                return line
        return None



