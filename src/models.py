from config import setting
import pickle
import os
from lib.commons import create_uuid


class Base:
    db_path = 'base'

    def __init__(self, name):
        self.name = name
        self.id = create_uuid()
        self.save()

    def __str__(self):
        return self.name

    def save(self):
        path = os.path.join(self.db_path, self.id)
        f = open(path, 'wb')
        pickle.dump(self, f)


    @classmethod
    def get_obj_by_id(cls,id):
        try:
            f = open(os.path.join(cls.db_path,id),'rb')
        except Exception as e:
            print(e)
        else:
            obj = pickle.load(f)
            return obj

    @classmethod
    def get_obj_by_name(cls,name):
        l = os.listdir(cls.db_path)
        for item in l:
            f=open(os.path.join(cls.db_path,item),'rb')
            obj = pickle.load(f)
            if obj.name == name:
                return obj
        else:
            print('Sorry, not found')

    @classmethod
    def get_id_by_name(cls,name):
        l = os.listdir(cls.db_path)
        for item in l:
            f=open(os.path.join(cls.db_path,item),'rb')
            obj = pickle.load(f)
            if obj.name == name:
                return obj.id
        else:
            print('Sorry, not found')




    @classmethod
    def get_all(cls):
        l = []
        path = os.path.join(cls.db_path)
        for item in os.listdir(path):
            f = open(os.path.join(cls.db_path, item), 'rb')
            school_obj = pickle.load(f)
            l.append(school_obj)
        return l

class School(Base):
    db_path = setting.SCHOOL_DB


class Classes(Base):
    db_path = setting.CLASSES_DB

    def __init__(self,name,school_id): #在主函数时候获取关联id
        self.school_id = school_id
        super().__init__(name)




class Course(Base):
    db_path = setting.COURSE_DB


if __name__ == '__main__':
    s1 = School('beida')
    s2 = School('qinghua')
    print(s1.id,s1.name,s2.id,s2.name)

    c1 = Classes('shuxue','beida')
    print(c1.id,c1.name,c1.school_id)
    c2 = Classes('yuwen','qinghua')
    print(c2.id,c2.name,c2.school_id)


    c = Classes.get_obj_by_name('shuxue')
    print(c.id,c.name,c.school_id)