# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1097, 760)
        MainWindow.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(460, 510, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 450, 66, 19))
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(350, 430, 321, 51))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(340, 260, 331, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 600, 751, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.toolButton_file_select = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_file_select.setGeometry(QtCore.QRect(990, 20, 101, 41))
        self.toolButton_file_select.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 118, 118);")
        self.toolButton_file_select.setObjectName("toolButton_file_select")
        self.toolButton_ses = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_ses.setGeometry(QtCore.QRect(690, 360, 71, 41))
        self.toolButton_ses.setStyleSheet("background-color: rgb(118, 118, 118);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("1486485571-198high-loud-music-on-sound-speaker-volume_81180.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_ses.setIcon(icon)
        self.toolButton_ses.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_ses.setObjectName("toolButton_ses")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(380, 150, 256, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.toolButton_help = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_help.setGeometry(QtCore.QRect(990, 80, 101, 26))
        self.toolButton_help.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 118, 118);")
        self.toolButton_help.setObjectName("toolButton_help")
        self.toolButton_back = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_back.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.toolButton_back.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(118, 118, 118);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("back_white_button_icon_227869.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_back.setIcon(icon1)
        self.toolButton_back.setObjectName("toolButton_back")
        self.radioButton_siraylaSor = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_siraylaSor.setGeometry(QtCore.QRect(990, 170, 111, 25))
        self.radioButton_siraylaSor.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_siraylaSor.setObjectName("radioButton_siraylaSor")
        self.pushButton_result = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_result.setGeometry(QtCore.QRect(990, 120, 101, 27))
        self.pushButton_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(118, 118, 118);")
        self.pushButton_result.setObjectName("pushButton_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1097, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PUSH"))
        self.label.setText(_translate("MainWindow", "CEVAP:"))
        self.toolButton_file_select.setText(_translate("MainWindow", "dosya seç"))
        self.toolButton_ses.setText(_translate("MainWindow", "..."))
        self.toolButton_help.setText(_translate("MainWindow", "help"))
        self.toolButton_back.setText(_translate("MainWindow", "..."))
        self.radioButton_siraylaSor.setText(_translate("MainWindow", "Sırayla  sor"))
        self.pushButton_result.setText(_translate("MainWindow", "Sonuçlar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())