import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

try:
	try:
		read_check = (open("py_files/secret_info.txt","r").read()).split(' ')
		if len(read_check) == 0:
			os.system("python py_files/login.py")
			
		else:
			os.system("python py_files/main_window.py")
	except Exception as e:

		os.system("python py_files/login.py")
except Exception as e:
	print(e)
