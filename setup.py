import subprocess
import sys
import time
from __dwnldDrivers.versions import *


def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])


def main():

    my_packages = ['pyqt5', 'pandas', 'numpy', 'selenium', 'keyboard']

    installed_pr = []

    for package in my_packages:
        install(package)
        print('\n')

    print('Chrome')
    chrome_ver = get_chrome_version()

    if chrome_ver != None:
        is_chrome_there = 1
        installed_pr.append('Chrome')
        setup_Chrome(chrome_ver)
    else:
        is_chrome_there = 0
        print('Chrome isn\'t installed')

    if is_chrome_there == 0:
        print('Error - Setup installation failed \nReason - Please install Chrome browser to complete setup process')
        exit()

    for index, pr in enumerate(installed_pr, start=1):
        print('\n[*] ' + str(index) + ' ' + pr)

    print('Setup Completed, This window will be automatically closed after 10 seconds')
    time.sleep(10)


if __name__ == '__main__':
    main()
