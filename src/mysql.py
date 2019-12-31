import pymysql

class Mysql:

    def __init__(self, host='localhost',user='root',password='12345678',
                 database='test',port=3306,charset='utf8',cursorclass=pymysql.cursors.DictCursor):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.cursorclass = cursorclass
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pymysql.connect(self.host,self.user,self.password,self.database,
                                    self.port,charset=self.charset,cursorclass=self.cursorclass)
        except:
            print('connection failed')
            return False
        else:
            self.cursor = self.conn.cursor()
            return True

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


    def execute(self,sql):
        if self.conn and self.cursor:
            # sql = 'select * from student where id=3'
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data


# conn = pymysql.connect(host='localhost',
#                        port=3306,
#                        user='root',
#                        password='12345678',
#                        database='test',
#                        charset='utf8',
#                        cursorclass=pymysql.cursors.DictCursor)





def insert(table, values):
    sql = 'insert into '+table+' (name,age,gender) values(%s,%s,%s)'
    cursor.execute(sql,values)
    conn.commit()


def get_all(table):
    sql = 'select * from '+table
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_one(table, condition):
    sql = "select * from "+table+" where id=%s"
    print(sql)
    cursor.execute(sql,(condition,))
    data = cursor.fetchone()
    return data


def update(table, condition):
    sql = 'update ' + table + ' set ' + condition
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    obj = Mysql()
    obj.connect()
    r = obj.execute('update student set name="alexup" where id=3')
    obj.conn.commit()
    print(r)
