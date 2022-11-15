age = 17

try:
    assert age>=18
except AssertionError:
    print("age must me greater or equals to 18")
except Exception as e:
    print(e)
