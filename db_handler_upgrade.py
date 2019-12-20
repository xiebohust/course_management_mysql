import pymysql


class Mysql:
    def __init__(self,host='localhost',user='root',passwd='12345678',db='test'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = pymysql.connect(user=self.user, passwd=self.passwd,host=self.host,db=self.db)
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)


    def close(self):
        self.cursor.close()
        self.conn.close()


    def query(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)


    def insert(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()




if __name__ == "__main__":


    obj = Mysql('localhost','root','12345678','test')
    obj.query('select * from account where id=2')
    obj.query('select * from account where id=1')
    obj.insert("insert into account (username,password) values('c','c')")
    obj.close()