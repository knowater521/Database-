# coding:utf-8
from MySQLdb import *

# try:
# 创建Connection对象
coon = connect(host='localhost', user='linfapeng', passwd='lfp930623', db='python3', port=3306, charset='utf8')
# 创建Cursor对象
cursor1 = coon.cursor()

# 删除数据
# sql = "delete from students where name='koko'"
# cursor1.execute(sql)
# coon.commit()

# 插入数据
# name = raw_input("请输入要插入的名字:")
# sql = "insert students(name) values(%s)"
# # 参数化，防止SQL注入攻击
# cursor1.execute(sql, [name])
# coon.commit()

# 查询数据
# sql = "select * from students"
# result1 = cursor1.execute(sql)
# result = cursor1.fetchall()
# print(result)

cursor1.close()
coon.close()
print('成功！')

# except Exception, e:
#     print(e.message)




