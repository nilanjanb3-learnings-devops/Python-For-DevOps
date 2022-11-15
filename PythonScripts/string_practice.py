import os
s = "welcome to python scripting"
a = os.get_terminal_size().columns
columns = int(a)
print(s.center(columns))
print(s.rjust(columns))
print(s.ljust(columns))
