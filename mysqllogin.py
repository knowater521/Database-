# coding:utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1


def addin():
    print("-----欢迎注册-----")
    while True:
        name = raw_input("请输入用户名：")
        # 注册
        user1 = MysqlHelper('localhost', 3306, 'linfapeng', 'lfp930623', 'python3')
        # 查询当前所有用户名
        sqlname = 'select uname  from userinfos'
        result = user1.get(sqlname)
        for item in result:
            if item[0] == name:
                print('用户名已存在，请重新输入!')
                break
        else:
            passwd1 = raw_input("请输入密码：")
            break

    # 对密码加密
    m = sha1()
    m.update(passwd1)
    passwdsha1 = m.hexdigest()

    sql = 'insert userinfos(uname,upwd) values(%s,%s)'
    params = [name, passwdsha1]
    user1.cud(sql, params)


def login():
    print("-----欢迎登录-----")
    name = raw_input("请输入用户名：")
    passwd = raw_input("请输入密码：")
    # 对密码加密
    m = sha1()
    m.update(passwd)
    passwdsha1 = m.hexdigest()
    # 实例化
    user1 = MysqlHelper('localhost', 3306, 'linfapeng', 'lfp930623', 'python3')
    # 查询当前所有用户名
    sql = 'select upwd from userinfos where uname=%s'
    result = user1.get(sql, [name])
    # print(result)
    if len(result) == 0:
        print('用户名错误！')
    elif result[0][0] == passwdsha1:
        print('登录成功！')
    else:
        print('密码错误！')

login()