"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: ExcelUtil.py
    @time: 2019-10-22 17:02
    @desc: 
"""
import os

import xlrd


class SheetTypeError(object):
    pass


class ExcelReader:
    def __init__(self, excel_file, sheet_by):
        if os.path.exists(excel_file):
            self.excel_file = excel_file
            self.sheet_by = sheet_by
            self._data = list()
        else:
            raise FileNotFoundError("文件不存在")

    def data(self):
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_file)
            if type(self.sheet_by) not in [str, int]:
                raise SheetTypeError("请输入Int or Str")
            elif type(self.sheet_by) == int:
                sheet = workbook.sheet_by_index(self.sheet_by)
            elif type(self.sheet_by) == str:
                sheet = workbook.sheet_by_name(self.sheet_by)

            # 读取sheet内容
            # 返回list 元素：字典
            # 获取首行信息
            title = sheet.row_values(0)
            # print(title)
            # 遍历测试行，与首行组成dict，放在list中
            for row in range(1, sheet.nrows):
                row_value = sheet.row_values(row)
                # print(row_value)
                # 与首行组成字典，放list
                self._data.append(dict(zip(title, row_value)))
        return self._data


if __name__ == '__main__':
    reader = ExcelReader("../data/testdata.xlsx", "美多商城接口测试")
    print(reader.data())