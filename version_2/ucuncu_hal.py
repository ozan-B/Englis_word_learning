from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore ,QtGui
from kelimem_copy import Ui_MainWindow
import pandas as pd
import random
import os
import pyttsx3
#from anasayfa_python import Anasayfa



'''class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)

        self.veri = pd.read_excel('kelimeler.ods')
        self.ingilizce_sutun = 'English'
        self.turkce_sutun = 'Turkish'

        self.sorulan_kelime = self.ekran_kelime_yaz()

        self.ui.pushButton.clicked.connect(self.Cevapla)
'''
'''Bu satırlar, betiğin doğrudan çalıştırılıp çalıştırılmadığını kontrol eder ve ardından
 Main sınıfının bir örneğini oluşturarak uygulamayı başlatır. Eğer bu satırları silerseniz,
  bu kodu daha büyük bir uygulamanın parçası olarak kullanacaksanız veya başka bir betikten 
çalıştıracaksanız, Main sınıfının bir örneğini oluşturup uygulamayı başlatmanız gerekecektir.
 Eğer bu betik bağımsız bir uygulama olarak kullanılacaksa, bu satırları silebilirsiniz.
'''

class Ucuncu_hal_Page(QtWidgets.QMainWindow, Ui_MainWindow):

    
    def __init__(self):
        super().__init__()       #super()fonksiyonu, üst sınıfın (QtWidgets.QMainWindow) metotlarına erişimi sağlar. __init__ metodu, üst sınıfın yapıcı metodunu çağırarak, üst sınıfın başlatılmasını gerçekleştirir.Bu, Main sınıfının QtWidgets.QMainWindow sınıfının özelliklerini ve davranışlarını devralmasını sağlar.
        self.setupUi(self)      #Ui_MainWindow sınıfının setupUi metodunu çağırarak kullanıcı arayüzünün kurulumunu gerçekleştirir.


        self.baslik_yaz()


        # Dosya seçme ekranını açacak buton
        self.toolButton_file_select.clicked.connect(self.open_file_dialog)
        


        self.veri = None  #self.veri, okunan Excel verilerini içeren bir pandas DataFrame objesidir. DataFrame, veri tablolarını temsil etmek için pandas kütüphanesinde kullanılan bir veri yapısıdır.
        self.ucuncu_hal_sutun = 'third'
        self.birinci_hal_sutun = 'first'





        self.sorulan_kelime = None #Bu satır, self.sorulan_kelime adlı bir özelliği oluşturur ve bu özelliğe başlangıçta None değerini atar. Bu özellik, kullanıcıya sorulan kelimenin geçici olarak saklanması için kullanılır.
        self.secilen_index = None


        self.pushButton.clicked.connect(self.Cevapla)#kullanıcı arayüzündeki bir butona (self.pushButton) tıklandığında self.Cevapla adlı bir metodun çağrılmasını sağlar. Yani, bu satır, butonun tıklanma olayını (clicked event) self.Cevapla metoduna bağla
        self.lineEdit.returnPressed.connect(self.Cevapla)  # QLineEdit'da Enter tuşuna basıldığında Cevapla adlı methodu çağır
                                                           #lineEdit özelliği, kullanıcıdan metin girişi almak için tasarlanmış bir QLineEdit öğesini temsil eder.

        
        self.ekran_kelime_yaz_rastgele()

        self.pushButton.clicked.connect(self.temizle)  #butona her basıldığında texbrowser_2 yi temizler.
        self.lineEdit.returnPressed.connect(self.temizle)  #entera her basıldığında texbrowser_2 yi temizler.                           
        
 
        self.toolButton_ses.clicked.connect(self.oku) #butona tıklandığında kelime okunur.

        self.toolButton_help.clicked.connect(self.help)

        #self.toolButton_back.clicked.connect(self.anasayfa_giris)
        #self.anasayfa_acc = Anasayfa()

    def ekran_kelime_yaz_rastgele(self):
        
        if self.veri is not None:

            #rastgele bir index seç
            self.secilen_index = random.randint(0, len(self.veri) - 1)

            #Seçilen indexteki ingilizce kelimeyi al
            self.sorulan_kelime = self.veri.loc[self.secilen_index, self.birinci_hal_sutun]

            # Sorulan kelimeyi textBrowser'a göster
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

    #def ekrana_kelime_yaz_sırayla()


    def Cevapla(self):
        # QLineEdit öğesinden kullanıcının girdiği cevabı al
        cevap = self.lineEdit.text()


         # Doğru cevap kontrolü
        dogru_cevap = self.veri.loc[self.secilen_index, self.ucuncu_hal_sutun] #Bu satır, doğru cevabın, seçilen kelimenin second karşılığını (self.ucuncu_hal_sutun) içeren veri çerçevesinden (self.veri) alır ve dogru_cevap adlı bir değişkene atar. İşte daha ayrıntılı açıklama:
         #.loc[self.secilen_index, self.ucuncu_hal_sutun]: Bu ifade, self.veri veri çerçevesinin belirli bir konumundan veri seçer. self.secilen_index indeksi ve self.ucuncu_hal_sutun sütun adı kullanılarak, seçilen kelimenin Türkçe karşılığını (dogru_cevap) alır.

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



            self.ekran_kelime_yaz_rastgele()


        else:

            # TextBrowser_2'nin metin rengini ve boyutunu değiştir
            text_color = QtGui.QColor(255, 0, 0)  # Örneğin, kırmızı renk
            font = QtGui.QFont()
            font.setPointSize(20)  # Örneğin, font boyutunu 14 olarak ayarla
            char_format = QtGui.QTextCharFormat()
            char_format.setForeground(text_color)
            char_format.setFont(font)
            self.textBrowser_2.setCurrentCharFormat(char_format)

            # Yanlış cevap durumunda metni oluştur
            metin = f"<font color='red' style='font-size: 20px;'>Yanlış cevap! Doğru cevap: </font><span style='color: yellow; font-size: 20px; font-weight: bold;'>       {dogru_cevap}     </span><font color='red' style='font-size: 20px;'> Tekrar deneyin.</font>"
 
            # QTextBrowser'ın içeriğini ayarla
            self.textBrowser_2.setHtml(metin)

            #self.textBrowser_2.setPlainText(f"Yanlış cevap! Doğru cevap:    {dogru_cevap}      Tekrar deneyin.") #bu kadu çalıştırmak istiyorsan 135 ve 138. satırları yorum satırına al
            

            # Yanlış cevap durumunda butonun rengini değiştir
            button_color = QtGui.QColor(255, 0, 0)  # Örneğin, mavi renk
            button_palette = self.pushButton.palette()
            button_palette.setColor(QtGui.QPalette.ButtonText, button_color)
            self.pushButton.setPalette(button_palette)


    def temizle(self):
        self.lineEdit.clear()


    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(self, "Dosya Seç", "", "Tüm Dosyalar (*);;(*.xlsx);;(*.ods)", options=options)
               
                       
        
        if file_name:
               
                               
            # Dosya adını ve uzantısını ayır
            dosya_adı, uzanti = os.path.splitext(file_name)
               
            if uzanti == '.exe' or uzanti == '.ods':
               
                # Seçilen dosyanın adını sadece döndür
               
                self.veri = pd.read_excel(file_name)
                self.ekran_kelime_yaz_rastgele()
                    
               
            else:
                # Yanlış uzantı için hata mesajı göster
                QMessageBox.warning(self, "Hata", "Lütfen geçerli bir Excel (.xlsx) veya ODS (.ods) dosyası seçin.")

                           
    def oku(self):

        # pyttsx3 kullanarak metni ses olarak çal
        engine = pyttsx3.init()
    

        """RATE"""       
        rate = engine.getProperty('rate')                           
        engine.setProperty('rate', 160)  

        """VOLUME"""
        volume = engine.getProperty('volume')                            
        engine.setProperty('volume',0.8)

        """VOICE"""
        voices = engine.getProperty('voices')       
        engine.setProperty('voice', 'espeak') #eSpeak ses motorunu kullanıyorum
        
        
        metin = self.sorulan_kelime

        engine.say(metin)
        engine.runAndWait()

                         
    def baslik_yaz(self):
        # Yanlış cevap durumunda metni oluştur
        metin = f"<div style='text-align: center;'><font color='red' style='font-size: 20px;'></font><span style='color: yellow; font-size: 20px; font-weight: bold;'>Üçüncü hali</span></div><font>"

        # QTextBrowser'ın içeriğini ayarla
        self.textBrowser_3.setHtml(metin)
            
    def help(self):

        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Bilgi")
        message_box.setText("Excel dosyanızda iki sütun olacak .Birinci sütunun adı 'first' , ikinci Sütunun adı 'third' olmalıdır. Program size fiilin birinci halini vericek siz de üçüncü halini cevap olarak yazıcaksınız.")
        message_box.exec_()



    '''def anasayfa_giris(self):   
                    self.hide()
                    self.anasayfa_acc.show()'''




if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    pencere = Ucuncu_hal_Page()
    pencere.show()


    
    sys.exit(app.exec_())