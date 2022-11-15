a = "Python"

# print(a.startswith('P'))

# print(a.endswith('x'))

res = a.islower()
res = a.isalpha()

res = a.isspace()

res = a.istitle()

a = "123"

res = a.isnumeric()

res = a.isalnum()
# print(res)

# =========== zfill, center, join =========
s = "hello welcome to python"

# print("-".join(s))

# print(s.center(20))
# print(s.center(40))

# print(s.zfill(50))


# ========= strip, split ============

words = s.split(" ")

print(words)

text = "     pythonxxx"

# print(text.strip())

print(text.lstrip().rstrip('x'))
