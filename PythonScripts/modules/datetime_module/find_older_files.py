from datetime import datetime as dt
import os
import sys
import time

curr_epoch_time = time.time()
th_time = 60*60*24

target_path = input("Enter path: ")
if(os.path.exists(target_path)):
    if(os.path.isdir(target_path)):
        for each_dir in os.listdir(target_path):
            each_file_path = os.path.join(target_path,each_dir)
            if(os.path.isfile(each_file_path)):
                # print(each_file_path)
                time_diff = curr_epoch_time - os.path.getctime(each_file_path)
                if(time_diff>th_time):
                    print(each_file_path)
    else:
        print("please enter a directory path".title())

else:
    print("you have entered a wrong path, please try again with a valid path".title())