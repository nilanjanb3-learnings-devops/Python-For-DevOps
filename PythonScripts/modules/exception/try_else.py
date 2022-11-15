try:
    print(a)
except ZeroDivisionError:
    print('zero division error')
except NameError:
    print('variable not defined')
except Exception as e:
    print(e)
else:
    print('else only execute if there is no exception occured in try')

finally:
    print('always execute until exception is uncaught')