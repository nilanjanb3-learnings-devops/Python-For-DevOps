import csv

fo = open('/home/nilanjan/Desktop/Python For DevOps/PythonScripts/file/csv/new_info.csv', 'w', newline="")

writer = csv.writer(fo)

writer.writerow(['SL_NO','NAME','ROLL'])

writer.writerow(['1','Nilanjan','1'])

fo.close()