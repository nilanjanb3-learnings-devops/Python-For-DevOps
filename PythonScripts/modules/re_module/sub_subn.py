import re

text = "this is python tutorial, there are two major versions python2 and python3 in future python4 will come"
pattern = r"\bpython[23]?\b"


print(re.sub(pattern, 'pypy', text))

print(re.subn(pattern, 'pypy', text))

