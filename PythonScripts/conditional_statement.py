def case_1():
    return "opt 1"

def case_2():
    return "opt 2"


switch = {1:case_1(), 2:case_2()}


opt = eval(input("enter choice"))

print(switch[opt])
