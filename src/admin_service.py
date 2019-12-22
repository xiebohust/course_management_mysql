from src.models import School,Classes

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
    school_obj = School(name)
    school_obj.save()

def get_school_list():
    for i in School.get_all():
        print(str(i))


def create_class():
    name = input('input class name:')
    school_obj = Classes(name)
    school_obj.save()

def get_class_list():
    for i in Classes.get_all():
        print(str(i))

def create_course():
    name = input('input class name:')
    tuition = input('tuition:')
    school_id = input('school')
    # course_to_teacher_list = input('')
    # obj_school = models.Classes(name=name, tuition=tuition,school_id=school_id,course_to_teacher_list=course_to_teacher_list)
    # obj_school.save()

def get_course_list():
    pass

    # for obj_sch in models.Course.get_all():
    #     print(str(obj_sch))

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
