import subprocess

cmd = 'java -version'

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rt = sp.wait()

out,err = sp.communicate()

if(len(err) ==0):
    print("There are some error")
else:

    print(err.split('"')[1])