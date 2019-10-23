# -*- coding:utf-8 -*-
"""
    @author: 萝卜头
    @Wechat Contact: 905913095
    @project: InterAutoTest_W
    @file: MysqlUtil.py
    @time: 2019-10-22 16:35
    @desc: 
"""
from utils.LogUtil import my_log
import pymysql


class Mysql:
    def __init__(self, host, user, password, database, charset="utf8", port=3306):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def fetchone(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self,sql):
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    def __del__(self):
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()

if __name__ == '__main__':
    mysql = Mysql(
        "211.103.136.242",
        "test",
        "test123456", "meiduo",
        charset="utf8",
        port=7090
    )

    res = mysql.fetchall("select username,password from tb_users")
    print(res)


"""

# 1、导入pymysql包
import pymysql

# 2、连接mysql

conn = pymysql.connect(
    host="211.103.136.242",
    user="test",
    password="test123456",
    database="meiduo",
    charset="utf8",
    port=7090
)

# 3、获取执行sql的光标对象
cursor = conn.cursor()

# 4、执行sql
sql = "select username,password from tb_users"
cursor.execute(sql)
res = cursor.fetchone()
print(res)
# 5、关闭对象
cursor.close()
conn.close()
"""
