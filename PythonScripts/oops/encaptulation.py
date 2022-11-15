class Base(object):
    __x = 100


    def display(self):
        print(self.__x)



base = Base()
base.display()

# we can't call the below as it's private member
# print(base.__x)