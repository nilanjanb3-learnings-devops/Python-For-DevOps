def foo(**kargs):
    print(kargs)

    for k,v in kargs.items():
        print(f'{k}:\t{v}')


foo(value=10, PI=3.14, name='nilanjan')