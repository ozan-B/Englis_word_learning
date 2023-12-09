from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets, QtCore ,QtGui
from anasayfa import Ui_form
from eng_turk import Eng_turk_Page
from turk_eng import Turk_eng_Page
from ikinci_hal import Ikinci_hal_Page
from ucuncu_hal import Ucuncu_hal_Page

class Anasayfa(QWidget):
	def __init__(self) -> None:
		super().__init__()
		self.anasayyfa = Ui_form()
		self.anasayyfa.setupUi(self)
		self.eng_turk_ac = Eng_turk_Page()
		self.turk_eng_ac = Turk_eng_Page()
		self.ikinci_hal_ac = Ikinci_hal_Page()
		self.ucuncu_hal_ac = Ucuncu_hal_Page()
		self.anasayyfa.pushButton_eng_turk.clicked.connect(self.eng_turk_giris)
		self.anasayyfa.pushButton_turk_eng.clicked.connect(self.turk_eng_giris)
		self.anasayyfa.pushButton_ikinci_hal.clicked.connect(self.ikinci_hal_giris)
		self.anasayyfa.pushButton_ucuncu_hal.clicked.connect(self.ucuncu_hal_giris)

	def eng_turk_giris(self):	
		self.hide()
		self.eng_turk_ac.show()

	def turk_eng_giris(self):
		self.hide()
		self.turk_eng_ac.show()
	def ikinci_hal_giris(self):
		self.hide()
		self.ikinci_hal_ac.show()
	def ucuncu_hal_giris(self):
		self.hide()
		self.ucuncu_hal_ac.show()