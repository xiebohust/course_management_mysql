from config import setting
import pickle
import os
from lib.commons import create_uuid


class Base:
    db_path = 'base'
    def __init__(self, name):
        self.name = name
        self.id = create_uuid()

    def __str__(self):
        return self.name

    def save(self):
        path = os.path.join(self.db_path, self.name)
        f = open(path, 'wb')
        pickle.dump(self, f)

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
    # def __init__(self, name):
    #     self.name = name
    #
    #
    # def save(self):
    #     path = os.path.join(self.db_path,self.name)
    #     f = open(path, 'wb')
    #     pickle.dump(self,f)
    #
    # @classmethod
    # def get_all(cls):
    #     l = []
    #     path = os.path.join(cls.db_path)
    #     for item in os.listdir(path):
    #         f = open(os.path.join(cls.db_path, item),'rb')
    #         school_obj = pickle.load(f)
    #         l.append(school_obj)
    #     return l
    #
    #
    # def __str__(self):
    #     return self.name


class Classes(Base):
    db_path = setting.CLASSES_DB

    def __init__(self,name):
        super().__init__(name)
        self.school_id = None




if __name__ == '__main__':
    # sch_obj = School('henan')
    # print(sch_obj.id)
    #
    #
    # for i in School.get_all():
    #     print(str(i))
    class_obj = Classes('python')
    school_obj = School('henan')
    school_obj.save()
    class_obj.school_id = school_obj.id
    class_obj.save()
    print(class_obj.id,class_obj.school_id)