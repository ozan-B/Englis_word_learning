from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore ,QtGui
from kelime import Ui_MainWindow
import pandas as pd
import random

'''class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.veri = pd.read_excel('kelimeler.ods')
        self.ingilizce_sutun = 'English'
        self.turkce_sutun = 'Turkish'

        self.sorulan_kelime = self.ekran_kelime_yaz()

        self.ui.pushButton.clicked.connect(self.Cevapla)'''



class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.veri = pd.read_excel('kelimeler.ods')
        self.ingilizce_sutun = 'English'
        self.turkce_sutun = 'Turkish'

        self.sorulan_kelime = None
        self.secilen_index = None

        self.pushButton.clicked.connect(self.Cevapla)
        self.lineEdit.returnPressed.connect(self.Cevapla)  # QLineEdit'da Enter tuşuna basıldığında Cevapla fonksiyonunu çağır


        self.ekran_kelime_yaz()

    def ekran_kelime_yaz(self):
        self.secilen_index = random.randint(0, len(self.veri) - 1)
        self.sorulan_kelime = self.veri.loc[self.secilen_index, self.ingilizce_sutun]
        self.textBrowser.setPlainText(self.sorulan_kelime)  # Sorulan kelimeyi göster


        # Sorulan kelimenin konumunu değiştir
        alignment = QtCore.Qt.AlignCenter  # Örneğin, metni ortala
        self.textBrowser.setAlignment(alignment)


        # Sorulan kelimenin fontunu değiştir
        font = QtGui.QFont()
        font.setPointSize(29)  # Örneğin, font boyutunu 16 olarak ayarla
        font.setBold(True)    # Kalın yazı tipini kullan
        self.textBrowser.setFont(font)

        # Sorulan kelimenin rengini değiştir
        text_color = QtGui.QColor(0, 255, 255)  # Örneğin, kırmızı renk
        text_palette = self.textBrowser.palette()
        text_palette.setColor(QtGui.QPalette.Text, text_color)
        self.textBrowser.setPalette(text_palette)


    def Cevapla(self):
        cevap = self.lineEdit.text()


        # Doğru cevap kontrolü
        dogru_cevap = self.veri.loc[self.secilen_index, self.turkce_sutun]
        if cevap.lower() == dogru_cevap.lower():

            # TextBrowser_2'nin metin rengini ve boyutunu değiştir
            text_color = QtGui.QColor(0, 255, 0)  # Örneğin, kırmızı renk
            font = QtGui.QFont()
            font.setPointSize(20)  # Örneğin, font boyutunu 14 olarak ayarla
            char_format = QtGui.QTextCharFormat()
            char_format.setForeground(text_color)
            char_format.setFont(font)
            self.textBrowser_2.setCurrentCharFormat(char_format)


            self.textBrowser_2.setPlainText("Doğru cevap! Başka bir kelime soruluyor.")


            # Doğru cevap durumunda butonun rengini değiştir
            button_color = QtGui.QColor(0, 255, 0)  # Örneğin, mavi renk
            button_palette = self.pushButton.palette()
            button_palette.setColor(QtGui.QPalette.ButtonText, button_color)
            self.pushButton.setPalette(button_palette)



            self.ekran_kelime_yaz()
        else:

            # TextBrowser_2'nin metin rengini ve boyutunu değiştir
            text_color = QtGui.QColor(255, 0, 0)  # Örneğin, kırmızı renk
            font = QtGui.QFont()
            font.setPointSize(20)  # Örneğin, font boyutunu 14 olarak ayarla
            char_format = QtGui.QTextCharFormat()
            char_format.setForeground(text_color)
            char_format.setFont(font)
            self.textBrowser_2.setCurrentCharFormat(char_format)


            self.textBrowser_2.setPlainText(f"Yanlış cevap! Doğru cevap: {dogru_cevap}. Tekrar deneyin.")
            

            # Yanlış cevap durumunda butonun rengini değiştir
            button_color = QtGui.QColor(255, 0, 0)  # Örneğin, mavi renk
            button_palette = self.pushButton.palette()
            button_palette.setColor(QtGui.QPalette.ButtonText, button_color)
            self.pushButton.setPalette(button_palette)

            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pencere = Main()
    pencere.show()
    sys.exit(app.exec_())