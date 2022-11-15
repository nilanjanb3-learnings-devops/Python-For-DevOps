my_dict = {'name':"nilanjan", 'role':'DevOps', 'dob':21022000}


# print(my_dict['surname']) # Throw wxception
# print(my_dict.get("name")) # handle exception

# print(my_dict.keys())
# print(my_dict.values())

# print(my_dict.items())

# my_dict.pop('role')

# print(my_dict)
# my_dict.popitem()
# print(my_dict)

my_dict.update({'three':3})

# print(my_dict)

keys = ['a', 'b', 'c', 'd']

new_dict = dict.fromkeys(keys)

# print(new_dict.items())


x = {'a':'a', 'b':'b'}

print(x.setdefault('b',8))

print(x.setdefault('c','c'))

# After Python 3.7, dictionary is ordered