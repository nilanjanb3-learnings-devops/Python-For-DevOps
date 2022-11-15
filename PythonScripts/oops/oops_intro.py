class Student(object):

    def __init__(self):
        print('constructor called')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(f'name: {self.name}')

    def __del__(self):
        print('object has been deleted')
        return None



def main():
    nilanjan = Student()
    nilanjan.set_name('Nilanjan Bhattacharjee')
    nilanjan.get_name()


if (__name__ == '__main__'):
    main()