import csv

fo = open('/home/nilanjan/Desktop/Python For DevOps/PythonScripts/file/csv/sample.csv', 'r')

# Method 1
# content = csv.reader(fo)

# for each in content:
#     print(each)


# Method 2
# content = fo.read().split('\n')

# for each in content:
#     print(each.split(','))