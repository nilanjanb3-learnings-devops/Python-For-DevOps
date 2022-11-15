import os

path = '/home/nilanjan/Desktop/Python For DevOps/PythonScripts'

items = list(os.walk(path, topdown=False))

# print(items)

for root, dir_name, file_name in items:
    for each in file_name:
        print(os.path.join(root, each))
