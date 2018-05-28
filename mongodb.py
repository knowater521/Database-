# coding:utf-8
from pymongo import *

# 获得客户端建立连接
client = MongoClient('localhost', 27017)
# 切换数据库
db = client.py3
# 获取集合
stu = db.stu
# 增加数据
# s1 = stu.insert({'name': '张三丰', 'age': 100})
# 修改
# stu.update_one({'name': '张三丰'},{'$set':{'name':'abc'}})
# 删除
stu.delete_one({'name': 'abc'})
# 查询
cursor = stu.find({'age': {'$gt': 15}})
# for doc in cursor:
#     print doc['name'], doc['gender'], doc['age']

# s2 = stu.find_one({'name': 'hr'})
# print s2

# cursor = stu.find().sort('age', DESCENDING)
# for doc in cursor:
#     print doc

# cursor = stu.find().sort([('age', DESCENDING), ('name', ASCENDING)])
# for doc in cursor:
#     print doc

cursor = stu.find().skip(2).limit(3)
for doc in cursor:
    print doc
