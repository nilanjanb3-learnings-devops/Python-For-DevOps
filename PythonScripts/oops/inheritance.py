class Person(object):
    def __init__(self,name,dob):
        self.name = name
        self.dob = dob


class Student(Person):

    def __init__(self, name, dob, sid):
        Person.__init__(self, name, dob)
        self.sid = sid

    def display(self):
        print(f'{self.name}, {self.dob}, {self.sid}')



nilanjan = Student('nilanjan', '21022000', 1)

nilanjan.display()