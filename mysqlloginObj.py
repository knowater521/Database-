# coding:utf-8
from MysqlHelper import MysqlHelper
from hashlib import sha1


# 对密码加密
def jiami(passwd1):
    m = sha1()
    m.update(passwd1)
    passwdsha1 = m.hexdigest()
    return passwdsha1


class Addin:
    def __init__(self):
        self.name = ''
        self.passwd = ''
        self.coon = None

    # 接收用户输入的姓名密码
    def inputname(self):
        while True:
            self.name = raw_input("请输入用户名：")
            # 连接数据库
            self.coon = MysqlHelper('localhost', 3306, 'linfapeng', 'lfp930623', 'python3')
            # 查询当前所有用户名
            sqlname = 'select uname  from userinfos'
            result = self.coon.get(sqlname)
            for item in result:
                if item[0] == self.name:
                    print('用户名已存在，请重新输入!')
                    break
            else:
                passwd = raw_input("请输入密码：")
                self.passwd = jiami(passwd)
                break

    def save(self):
        sql = 'insert userinfos(uname,upwd) values(%s,%s)'
        params = [self.name, self.passwd]
        self.coon.cud(sql, params)

    def run(self):
        print("-----欢迎注册-----")
        self.inputname()
        self.save()


class Login:
    def __init__(self):
        self.name = ''
        self.passwd = ''
        self.coon = None

    def inputname(self):
        self.name = raw_input("请输入用户名：")
        passwd = raw_input("请输入密码：")
        self.passwd = jiami(passwd)

    def yanzheng(self):
        # 连接数据库
        while True:
            user1 = MysqlHelper('localhost', 3306, 'linfapeng', 'lfp930623', 'python3')
            # 查询用户名的密码
            sql = 'select upwd from userinfos where uname=%s'
            result = user1.get(sql, [self.name])
            # print(result)
            if len(result) == 0:
                print('用户不存在！')
                self.inputname()
            elif result[0][0] == self.passwd:
                print('登录成功！')
                break
            else:
                print('密码输入错误！')
                self.inputname()

    def run(self):
        print("-----欢迎登录-----")
        self.inputname()
        self.yanzheng()

user1 = Addin()
user1.run()
user2 = Login()
user2.run()



