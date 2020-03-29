import pandas as pd
import pymysql as mysql

sql_cmd = 'select * from hd_insurance_policy_t'  # 输入你的SQL语句
connection = mysql.connect(host='47.103.87.53', port=3306, user='test', password='ztmT33ZC8ZMfPhKk', db='taiping_test',
                           charset='utf8')  # 创建数据库链接属性
data = pd.read_sql(sql=sql_cmd, con=connection)  # 导入数据库查结果为DataFrame
filePath = pd.ExcelWriter("sql.xlsx")# 创建excel
data.to_excel(filePath,encoding="utf-8") # dataframe转换为excel
filePath.save() #保存excel
