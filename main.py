import db_handler_upgrade

class Admin:
    def __init__(self,user,password):
        self.user = user
        self.password = password


    def create_student(self):
        name = input('name:')
        age = input('age:')
        gender = input('gender:')
        db_handler_upgrade.Mysql().insert('insert into student (name,age,gender) values(%s,%s,%s)' %(name,age,gender))

    def delete_student(self):
        pass

    def change_student(self):
        pass

    def query_student(self):
        pass

    def query_all_student(self):
        pass

    def logout(self):
        pass


def show():
    print("""
学生管理系统  v1.0
 1.添加学生的信息
 2.删除学生的信息
 3.修改学生的信息
 4.查询学生的信息
 5.遍历所有学生的信息
 6.退出系统
 """)

def actions(admin):
    action_dict = {
        '1':admin.create_student,
        '2':admin.delete_student,
        '3':admin.change_student,
        '4':admin.query_student,
        '5':admin.query_all_student,
        '6':admin.logout
    }
    return action_dict

def interactive():
    while True:
        admin = Admin('123', '123')
        show()
        choice = input('输入你要进行的操作：')
        if choice in actions(admin):
            actions(admin)[choice]()
        else:
            print('请输入正确操作')



if __name__ == "__main__":
    interactive()
