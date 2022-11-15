import shutil
src = "/home/nilanjan/Desktop/Python For DevOps/sample.txt"
dst = "/home/nilanjan/Desktop/Python For DevOps/sample.backup"

shutil.copy2(src, dst)

shutil.copymode()