import pandas
import xlwt

#导入excel表格

excel_data = pandas.read_excel("D:\Irving'sFiles\work\国任衡度项目\北汽\延保项目任务清单.xlsx",sheet_name="Sheet1")

data = pandas.DataFrame(excel_data)

data = data.fillna("")
print(data)