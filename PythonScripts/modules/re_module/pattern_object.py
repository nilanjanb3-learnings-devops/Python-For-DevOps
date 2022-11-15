import re
text = "this is python tutorial, there are two major versions python2 and python3 in future python4 will come"

pattern = r"\bpython[23]?\b"

# pattern object has higher efficiency than simple re functions

pat_obj = re.compile(pattern, flags=re.I)


print(pat_obj.search(text).group())