# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfam.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(901, 561)
        self.verticalLayoutWidget = QtWidgets.QWidget(form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 130, 661, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_eng_turk = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_eng_turk.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_eng_turk.setMouseTracking(False)
        self.pushButton_eng_turk.setCheckable(False)
        self.pushButton_eng_turk.setChecked(False)
        self.pushButton_eng_turk.setObjectName("pushButton_eng_turk")
        self.verticalLayout.addWidget(self.pushButton_eng_turk)
        self.pushButton_turk_eng = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_turk_eng.setObjectName("pushButton_turk_eng")
        self.verticalLayout.addWidget(self.pushButton_turk_eng)
        self.pushButton_ikinci_hal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ikinci_hal.setObjectName("pushButton_ikinci_hal")
        self.verticalLayout.addWidget(self.pushButton_ikinci_hal)
        self.pushButton_ucuncu_hal = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_ucuncu_hal.setObjectName("pushButton_ucuncu_hal")
        self.verticalLayout.addWidget(self.pushButton_ucuncu_hal)
        self.textBrowser = QtWidgets.QTextBrowser(form)
        self.textBrowser.setGeometry(QtCore.QRect(280, 50, 351, 71))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.pushButton_eng_turk.setText(_translate("form", "İngilizce_Türkçe"))
        self.pushButton_turk_eng.setText(_translate("form", "Türkçe-İngilizce"))
        self.pushButton_ikinci_hal.setText(_translate("form", "İkinci hali"))
        self.pushButton_ucuncu_hal.setText(_translate("form", "Üçüncü hali"))
        self.textBrowser.setHtml(_translate("form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; color:#8ff0a4; vertical-align:super;\">               ANASAYFA</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
