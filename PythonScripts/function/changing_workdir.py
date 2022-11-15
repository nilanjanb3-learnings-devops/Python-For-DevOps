import os

def change_dir():
    req_path = input('enter the path: ')
    if(os.path.exists(req_path)):

        os.chdir(req_path)
        print(os.curdir)
    else:
        raise Exception('Directory not exist')


if(__name__ == '__main__'):
    try:
        change_dir()
    except Exception as e:
        print(f'Exception occured: {e}')