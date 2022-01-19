import subprocess
import sys
import time

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])

def main():

    my_packages = ['pyqt5', 'pandas', 'numpy', 'selenium', 'keyboard']

    installed_pr = [] 
    
    for package in my_packages:
        install(package)
        print('\n')

    for index, pr in enumerate(installed_pr, start=1):
        print('\n[*] ' + str(index) + ' ' + pr)

    print('Setup Completed, This window will be automatically closed after 10 seconds')
    time.sleep(10)
if __name__ == '__main__':
    main()