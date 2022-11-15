import re

text = "this is python tutorial, there are two major versions python2 and python3 in future python4 will come"
pattern = r"\bpython[23]?\b"


for each in re.finditer(pattern, text):
    print(f'{each.group()}\tstart: {each.start()}\tend: {each.end()}')