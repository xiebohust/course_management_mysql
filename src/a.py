import uuid
import pickle

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


class School:
    db_path = os.path.join(BASE_DIR,'school')

    def __init__(self,name):
        self.name = name
        self.id = str(uuid.uuid1())


    def __str__(self):
        return self.name

    def save(self):
        f = open(os.path.join(self.db_path,self.id),'wb')
        pickle.dump(self,f)
        f.close()

    @staticmethod
    def get(path):
        f = open(path,'rb')
        obj = pickle.load(f)
        return obj

    @classmethod
    def get_all_objs(cls):
        l = []
        for name in os.listdir(cls.db_path):
            f = open(os.path.join(cls.db_path,name),'rb')
            obj = pickle.load(f)
            l.append(obj)
        return l

class Student(School):
    db_path = os.path.join(BASE_DIR,'student')

    def __init__(self,name,school_id):
        self.name = name
        self.id = str(uuid.uuid1())
        self.school_id = school_id


# School1 = School('beijing')
# print(School1.name,School1.id)
# School1.save()
# obj1 = School.get(School1.id)
# print('obj1',obj1.name,obj1.id)

if __name__ == "__main__":


    s = 'nihao {name} {age}'.format(name='alice',age=12)
    print(s)