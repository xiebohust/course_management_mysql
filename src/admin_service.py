from src.models import School,Classes,Course,Teacher

menu = """
1.创建学校
2.查看学校
3.创建班级
4.查看班级
5.创建课程
6.查看课程
"""

def create_school():
    name = input('input school name:')
    School(name)


def get_school_list():
    School.get_all()


def create_class():
    school_name = input('school name:')
    name = input('input class name:')
    Classes(name,school_name)

def get_class_list():
    Classes.get_all()

def create_course():
    name = input('input class name:')
    tuition = input('tuition:')
    school_id = input('school')


def get_course_list():

    Course.get_all()

action_list = {
    '1':create_school,
    '2':get_school_list,
    '3':create_class,
    '4':get_class_list,
    '5':create_course,
    '6':get_course_list
}


def main():
    while True:
        print(menu)
        action = input('choose action:')
        if action in action_list:
            action_list[action]()





if __name__ == "__main__":
    main()
