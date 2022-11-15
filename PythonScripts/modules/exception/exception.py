
try:
    print(4/0)
# except:
#     print("zero division error")

# except Exception as e:
#     print(e)

except NameError:
    print("variable not defined")

except ZeroDivisionError:
    print("division by zero not possible")

except Exception as e:
    print(f"exception occured: {e}")

finally:
    print('after try and except block')