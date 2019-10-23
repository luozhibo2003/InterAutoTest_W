"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: excel_demo.py
    @time: 2019-10-22 16:54
    @desc: 
"""

# 1、导入包 xlrd
import xlrd
# 2、创建workbook对象
book = xlrd.open_workbook("testdata.xlsx")
# 3、sheet对象
sheet = book.sheet_by_index(0)
print(sheet)
sheet = book.sheet_by_name("美多商城接口测试")
print(sheet)
# 4、获取行数和列数
rows = sheet.nrows # 行数
cols = sheet.ncols # 列数

# 5、读取每行内容
for r in range(rows):
    r_values = sheet.row_values(r)
    # print(r_values)

# 6、读取每列的内容
for c in range(cols):
    c_values = sheet.col_values(c)
    # print(c_values)

# 7、读取固定列的内容
print(sheet.cell_value(1,1))

