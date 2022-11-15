import os
import sys

target_path = input("Enter path: ")
target_file = input("Enter file name: ")

for root, directories, files in os.walk(target_path):
    for each_file in files:
        if(each_file == target_file):
            print("========= file found! =========".center(os.get_terminal_size().columns))
            print("PATH: "+os.path.join(root,each_file))
            sys.exit()
else:
    print("file not found")
