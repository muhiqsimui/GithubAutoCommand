from dotenv import load_dotenv
import os
import json
import time

# ambil data .env
load_dotenv('.env')

# ambil data json
file_json = open("command.json")
data = json.loads(file_json.read())

# fungsi untuk mengambil command dari json sesuai name


def cmd(name):
    for index in data:
        if (index['name'] == name):
            return (index['command'])


def run(command):
    print('Running command.... ')
    time.sleep(1)
    os.system(command)

# print(cmd('commit'))

# untuk mengambil data sensitif
# a = os.getenv('TOKEN')

# akses command prompt
# os.system('ipconfig')

# cek apakah ada file yg dibutuhkan
# cek = os.path.exists('.env')
# print(cek)

# Author https://github.com/muhiqsimui


def cek_git():
    cekGit = os.path.exists('.git')
    if (cekGit):
        print('git founded, script continue')
    else:

        menu = True
        while (menu):
            ans = input(
                'Do you want to make file .git  : \n y/n : ')
            if (ans == 'y' and 'Y'):
                print('Creating file .git')
                time.sleep(2)
                # XCOMAND
                run(cmd('init'))
                menu = False
            elif (ans == 'n' and 'N'):
                print('bye')
                exit()
            else:
                print('only input y/n')


def menu_utama():
    username = str(input('Your github usename :\n'))
    print('example https://github.com/username/repo.git ')
    url_git = str(input("write git url for remote your git : "))

    time.sleep(2)
    print(f'Welcome {username}')
    time.sleep(2)
    garis = int(40)
    info = (garis*"~") + "\n MENU GIT \n" + '''
    1. git status
    2. git add
    3. git commit
    4. git push main
    5. git branch main
    6. git remote
    7. git fetch (MAINTENANCE)
    8. git rollback (MAINTENANCE)

    0. exit
    '''+(garis*"~")

    menu = True
    while (menu):
        print(info)
        pil = int(input("Input number : "))

        if(pil == 1):
            # XCOMAND
            run(cmd('status'))
        elif(pil == 2):
            # XCOMAND
            run(cmd('add'))
        elif(pil == 3):
            msg = str(input("write commit message : "))
            # XCOMAND
            run(cmd('commit') + msg)
        elif(pil == 4):
            # XCOMAND
            run(cmd('push'))
        elif(pil == 5):
            # XCOMAND
            run(cmd('branch'))
        elif(pil == 6):
            # XCOMAND
            run(cmd('remote')+url_git)
        elif(pil == 7):
            print('MAINTENANCE')
        elif(pil == 8):
            print('MAINTENANCE')
        elif(pil == 0):
            print('Thank you for use dont forget to follow github/muhiqsimui')
            exit()
        else:
            print('Only input menu number :)')


cek_git()
menu_utama()
