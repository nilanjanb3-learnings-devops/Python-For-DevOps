def fun():
    global x
    x = 100

def fun2():
    fun()
    print(x)


fun2()