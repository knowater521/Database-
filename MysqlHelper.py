# coding:utf-8
import MySQLdb


class MysqlHelper(object):
    def __init__(self, host, port, user, passwd, db, charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
        self.charset = charset

    # 打开连接
    def open(self):
        self.conn = MySQLdb.connect(host=self.host, port=self.port, db=self.db, user=self.user, passwd=self.passwd, charset=self.charset)
        self.cursor = self.conn.cursor()

    # 关闭连接
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 对数据库操作
    def cud(self, sql, params=[]):
        self.open()
        try:
            self.cursor.execute(sql, params)
            print('ok!')
        except Exception, e:
            print(e.message)
        self.conn.commit()
        self.close()

    # 查询操作
    def get(self, sql, params=[]):
        self.open()
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
        except Exception, e:
            print(e.message)
        self.close()
        return result




