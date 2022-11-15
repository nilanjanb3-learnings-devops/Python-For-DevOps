import csv

fo = open('/home/nilanjan/Desktop/Python For DevOps/PythonScripts/file/csv/sample.csv', 'r')

content = list(csv.reader(fo))

print(f"number os rows are: {len(content)-1}")
print(f'headers are: {content[0]}')

