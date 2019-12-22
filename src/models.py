from config import setting
import pickle
import os


class Base:
    db_path = 'base'
    def __init__(self, name):
        self.name = name

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

class School:
    db_path = setting.SCHOOL_DB
    def __init__(self, name):
        self.name = name


    def save(self):
        path = os.path.join(self.db_path,self.name)
        f = open(path, 'wb')
        pickle.dump(self,f)

    @classmethod
    def get_all(cls):
        l = []
        path = os.path.join(cls.db_path)
        for item in os.listdir(path):
            f = open(os.path.join(cls.db_path, item),'rb')
            school_obj = pickle.load(f)
            l.append(school_obj)
        return l


    def __str__(self):
        return self.name

if __name__ == '__main__':
    sch_obj = School('henan')
    sch_obj.save()


    for i in School.get_all():
        print(str(i))