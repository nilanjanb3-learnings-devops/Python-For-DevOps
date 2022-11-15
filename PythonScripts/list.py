a = [3,4, 3.14, False, "Hello", 3+4j]

# for item in a:
#     print(item)

# for i in range(0,len(a)):
#     print(a[i])


# print((a[1:4]))

# a.clear()

# print(a)

my_list = a

my_new_list = a.copy()

# print(id(a), id(my_list), id(my_new_list))

my_new_list.append(100)
my_new_list.insert(1, 44.55)



# print(my_new_list)

c = [1,2,3]

d = [4,5,6]

# c.append(d)
c.extend(d)
# print(c)
# c.remove(6)
print(c.pop(len(c)-1))
# print(c)

c.reverse()
print(c)

c.sort(reverse=True)
print(c)