# coding:utf-8
from MysqlHelper import MysqlHelper

helper1 = MysqlHelper('localhost', 3306, 'linfapeng', 'lfp930623', 'python3')
# 数据操作测试
# name = raw_input("请输入姓名:")
# sql = 'insert into students(name) values(%s)'
# helper1.cud(sql, [name])

# 查询操作测试
sql = 'select name,birthday,gender from students'
result = helper1.get(sql)
print(result)