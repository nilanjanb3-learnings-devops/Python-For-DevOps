import os,platform,time

def do_stuffs(operating_system):
    print('Please wait... cleaning the screen')
    time.sleep(2)
    if (operating_system == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')
    print('Please wait... loading the directories and files ')
    time.sleep(2)
    if(operating_system == 'Windows'):
        os.system('dir')
    else:
        os.system('ls -lart')


do_stuffs(str(platform.system()))


