from src.models import School,Classes,Course
from src.mysql import insert,get_all,get_one

menu = """
1.创建学校
2.查看所有学校
3.查询一个学校
4.创建班级
5.查看所有班级
6.查询一个班级
7.创建课程
8.查看所有课程
9.创建学生
10.查看所有学生
11.查看一个学生
"""

def show(lists):
    for index,item in enumerate(lists):
        print(index,str(item))


def create_school():
    name = input('input school name:')
    School(name)


def get_school_list():
    show(School.get_all())


def get_one_school():
    get_school_list()
    try:
        choose = int(input('choose your school index:'))
        school_obj = School.get_all()[choose]
    except Exception as e:
        print(e)
    else:
        print('学校信息：id:%s name:%s' %(school_obj.id,school_obj.name))


def create_class():
    get_school_list()
    try:
        choose = int(input('choose your school index:'))
        school_id = School.get_all()[choose].id
    except Exception as e:
        print(e)
    else:
        name = input('input class name:')
        Classes(name,school_id)

def get_class_list():
    show(Classes.get_all())

def get_one_class():
    get_class_list()
    try:
        choose = int(input('choose your class index:'))
        class_obj = Classes.get_all()[choose]
    except Exception as e:
        print(e)
    else:
        print('课程信息：id:%s name:%s school_id:%s school_name:%s' %(class_obj.id,class_obj.name,class_obj.school_id,School.get_obj_by_id(class_obj.school_id)))


def create_course():
    name = input('input class name:')
    tuition = input('tuition:')
    school_id = input('school')
    insert('student',(name,))


def get_course_list():
    show(Course.get_all())

def create_student():
    name = input('student name:')
    age = input('student age:')
    gender = input('student gender:')
    insert('student',(name,age,gender))



def get_student_list():
    for item in get_all('student'):
        print(item['id'],item['name'])

def get_one_student():
    type = input('要查询的条件：')
    value = input('查询值：')
    data = get_one('student',type+'='+value)
    print('查询结果',data)


action_list = {
    '1':create_school,
    '2':get_school_list,
    '3': get_one_school,
    '4':create_class,
    '5':get_class_list,
    '6': get_one_class,
    '7':create_course,
    '8':get_course_list,
    '9':create_student,
    '10':get_student_list,
    '11':get_one_student
}


def main():
    while True:
        print(menu)
        action = input('choose action:')
        if action in action_list:
            action_list[action]()





if __name__ == "__main__":
    main()
