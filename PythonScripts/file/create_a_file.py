# fo = open('random.txt', 'w')

# print(fo.writable())
# fo.write('first line')
# fo.write('same line')
# fo.write('\na new line')

# lines = ['first line', '\nsecond line', '\nthird line']
# fo.writelines(lines)


fo = open('random.txt', 'r')
# print(fo.read())
# print(fo.readline())
# print(fo.readlines())

print(fo.readline())
print(fo.readline())

fo.close()