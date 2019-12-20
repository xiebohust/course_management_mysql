

"""
创建北京、上海 2 所学校
创建linux , python , go 3个课程，linux py在北京开， go 在上海开
课程包含，周期，价格，通过学校创建课程
通过学校创建班级，班级关联课程、讲师
创建学员时，选择学校，关联班级
创建讲师角色时要关联学校，
提供两个角色接口
7.1. 学员视图，可以注册，交学费，选择班级，
7.2. 讲师视图，讲师可管理自己的班级，上课时选择班级，查看班级学员列表，修改所管理的学员的成绩
7.3. 管理视图，创建讲师，创建班级，创建课程
上面的操作产生的数据都通过pickle序列化保存到文件里
"""

class_list = []

class Admin:
    def __init__(self,user,password):
        self.user = user
        self.password = password


    def create_student(self):
        name = input('name:')
        age = input('age:')
        gender = input('gender:')
        obj_student = Student(name,age,gender)

    def create_class(self):
        name = input('name:')
        obj_class = Student(name)

class Classes:
    def __init__(self,name):
        self.name = name


class Student:

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.classes = None
        self.courses = None


    def select_classes(self):
        class_num = input('选择你的班级：')
        if class_num in class_list:
            self.classes = class_num
        else:
            print('错误班级')

    def pay_tuition(self):
        pass

