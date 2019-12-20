
class Admin:
    def __init__(self,user,password):
        self.user = user
        self.password = password


    def create_student(self):
        name = input('name:')
        age = input('age:')
        gender = input('gender:')

