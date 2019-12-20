#!/usr/bin/python
import pymysql


class SpiderPDO:
    def __init__(self):
        db_host = '127.0.0.1'
        db_user = 'root'
        db_pass = '12345678'
        db_name = 'test'
        conn = pymysql.connect(db_host, db_user, db_pass, db_name, charset='utf8')
        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    def execute(self, sql, params=None):
        return self.cursor.execute(sql, params)

    def fetch(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.fetchone()

    def fetchall(self, sql, params=None):
        self.execute(sql, params)
        return self.cursor.fetchall()

    def close(self):
        return self.cursor.close()

A = SpiderPDO()
e = A.execute('select * from account')
print(e)