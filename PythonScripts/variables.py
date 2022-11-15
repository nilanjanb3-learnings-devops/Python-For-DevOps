#python is a dynamically typed language

a = 10
print(a)
a = 23
print(a)

# del frees ram by deleting variable
# del a

print(a)

# id(a) will give the memory address
print(id(a))

b = 3.14
c = 2+5j

print(type(a))
print(type(b))
print(type(c))

e = 6;f = 4.5;g = 9+5j
print(e,f,g)

s = "welcome to python scripting"

print(s, type(s))

h = True

print(h, type(h))

# ========== Type Casting ============

x = 56
print(x,type(x))
y = str(x)
print(y,type(y))
z = bool(x)

print(z,type(z))

# boolean of empty is false
# everything can be converted to boolean

print(bool(""))
print(bool(None))
print(bool(0))
print(bool([]))

# everything can be converted to string but vice versa is not true

a = "102"
c = int(a)
print(c, type(c))


# printing multiple variables 

x = 3
y = 5.7

print("{}, {}, {}".format(x,y,a))
print(f"{x}, {y}, {a}")