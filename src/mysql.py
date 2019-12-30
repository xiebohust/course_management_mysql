import pymysql

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='12345678',
                       database='test',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)


cursor = conn.cursor()


def insert(table, values):
    sql = 'insert into '+table+' (name,age,gender) values(%s,%s,%s)'
    cursor.execute(sql,values)
    conn.commit()


def get_all(table):
    sql = 'select * from '+table
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def get_one(table,condition):
    sql = "select * from `%s` where id=%s"
    print(sql)
    cursor.execute(sql,(table,condition))
    data = cursor.fetchone()
    return data


def update(table,condition):
    sql = 'update ' + table + ' set ' + condition
    cursor.execute(sql)
    conn.commit()


if __name__ == '__main__':
    # r = get_one("student",'10')
    # print(r)
    sql ='select * from student where id=%s' %'10 or 1=1'
    print(sql)
    cursor.execute(sql)
    r= cursor.fetchall()
    print(r)

