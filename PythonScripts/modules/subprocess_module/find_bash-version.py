import subprocess

cmd = "bash --version"

sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rt = sp.wait()

out,err = sp.communicate()

if(len(err)!=0):
    print(f"The error is: {err}")
else:

    # print(out)
    # print(type(out))
    # out = str(out)
    i = out.index('version')
    s = i+8
    e = out.index('(')
    print(out[s:e])
