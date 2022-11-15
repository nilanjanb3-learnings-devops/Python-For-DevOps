import subprocess

# sp = subprocess.Popen(cmd, shell=True/False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
cmd = 'ls -lart' #only when shell is True
# cmd = ['ls', '-lart'] #only when shell is False
# Note: environment variables command doesn't work with shell=False
sp = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()

out,err = sp.communicate()

print(f'the output is {out}')
print(f'the error is {err}')