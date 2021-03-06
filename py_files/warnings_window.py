# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warnings.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 751)
        MainWindow.setMinimumSize(QtCore.QSize(781, 751))
        MainWindow.setMaximumSize(QtCore.QSize(781, 751))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 781, 751))
        self.main_frame.setStyleSheet("#main_frame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.w_label = QtWidgets.QLabel(self.main_frame)
        self.w_label.setGeometry(QtCore.QRect(290, 40, 201, 71))
        self.w_label.setStyleSheet("#w_label{    \n"
"    font: 57 22pt \"Google Sans\";\n"
"    background-color: rgb(219,68,55);\n"
"    color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"}\n"
"")
        self.w_label.setObjectName("w_label")
        self.label1 = QtWidgets.QLabel(self.main_frame)
        self.label1.setGeometry(QtCore.QRect(110, 150, 581, 91))
        self.label1.setStyleSheet("#label1{    \n"
"    font: 57 14pt \"Google Sans\";\n"
"\n"
"}\n"
"")
        self.label1.setObjectName("label1")
        self.driver_btn = QtWidgets.QPushButton(self.main_frame)
        self.driver_btn.setGeometry(QtCore.QRect(300, 220, 171, 41))
        self.driver_btn.setStyleSheet("#driver_btn{\n"
"background-color: rgb(15,157,88);\n"
"    font: 57 10pt \"Google Sans\";\n"
"border-radius:7px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#driver_btn:hover{\n"
"background-color: rgb(219,68,55);\n"
"\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.driver_btn.setObjectName("driver_btn")
        self.label2 = QtWidgets.QLabel(self.main_frame)
        self.label2.setGeometry(QtCore.QRect(110, 240, 481, 91))
        self.label2.setStyleSheet("#label2{    \n"
"    font: 57 14pt \"Google Sans\";\n"
"\n"
"}\n"
"")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.main_frame)
        self.label3.setGeometry(QtCore.QRect(320, 310, 151, 111))
        self.label3.setStyleSheet("#label3{    \n"
"    font: 57 14pt \"Google Sans\";\n"
"\n"
"}")
        self.label3.setObjectName("label3")
        self.frame = QtWidgets.QFrame(self.main_frame)
        self.frame.setGeometry(QtCore.QRect(200, 440, 341, 111))
        self.frame.setStyleSheet("background-image: url(:/newPrefix/assets/eg.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.eg_label = QtWidgets.QLabel(self.main_frame)
        self.eg_label.setGeometry(QtCore.QRect(170, 380, 41, 91))
        self.eg_label.setStyleSheet("#eg_label{    \n"
"    font: 57 14pt \"Google Sans\";\n"
"\n"
"}\n"
"")
        self.eg_label.setObjectName("eg_label")
        self.label_3 = QtWidgets.QLabel(self.main_frame)
        self.label_3.setGeometry(QtCore.QRect(100, 550, 601, 91))
        self.label_3.setStyleSheet("#label_3{    \n"
"    font: 57 14pt \"Google Sans\";\n"
"\n"
"}\n"
"")
        self.label_3.setObjectName("label_3")
        self.label4 = QtWidgets.QLabel(self.main_frame)
        self.label4.setGeometry(QtCore.QRect(100, 650, 601, 51))
        self.label4.setStyleSheet("#label4{    \n"
"    font: 57 14pt \"Google Sans\";\n"
"\n"
"}")
        self.label4.setObjectName("label4")
        self.find_btn = QtWidgets.QPushButton(self.main_frame)
        self.find_btn.setGeometry(QtCore.QRect(550, 650, 171, 41))
        self.find_btn.setStyleSheet("#find_btn{\n"
"background-color: rgb(15,157,88);\n"
"    font: 57 10pt \"Google Sans\";\n"
"border-radius:7px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"#find_btn:hover{\n"
"background-color: rgb(219,68,55);\n"
"\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.find_btn.setObjectName("find_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.driver_btn.clicked.connect(self.driver_tutorial)
        self.find_btn.clicked.connect(self.get_software)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.w_label.setText(_translate("MainWindow", "  Warnings!"))
        self.label1.setText(_translate("MainWindow", "1) Make Sure you have the latest chrome drive installed."))
        self.driver_btn.setText(_translate("MainWindow", "Driver Setup Tutorial"))
        self.label2.setText(_translate("MainWindow", "2) Make Sure your CSV file has these columns: "))
        self.label3.setText(_translate("MainWindow", "- First Name\n"
"- Last Name\n"
"- Email"))
        self.eg_label.setText(_translate("MainWindow", "eg:"))
        self.label_3.setText(_translate("MainWindow", "3) Never Share your downloaded version of the software\n"
"(for your security)."))
        self.label4.setText(_translate("MainWindow", "4) Get and share the software from here"))
        self.find_btn.setText(_translate("MainWindow", "Get Software"))

    def driver_tutorial(self):
        
        webbrowser.open("https://www.youtube.com/watch?v=o_ywzBnUCyU&t=4s")
    def get_software(self):
        webbrowser.open("https://github.com/DSC-UIT-khi/Google-DSC-Platform-Extension")
import pics_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
