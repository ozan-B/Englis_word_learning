from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5 import QtWidgets, QtCore ,QtGui
from anasayfam_interface import Ui_form
from options import Eng_turk_Page
from options import Turk_eng_Page
from options import Ikinci_hal_Page
from options import Ucuncu_hal_Page
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
		

	
	def anasayfa_show(self):
		self.show()

	def eng_turk_giris(self):	
		self.hide()
		self.eng_turk_ac.show()
		self.eng_turk_ac.toolButton_back.clicked.connect(self.anasayfa_show)

	def turk_eng_giris(self):
		self.hide()
		self.turk_eng_ac.show()
		self.turk_eng_ac.toolButton_back.clicked.connect(self.anasayfa_show)

	def ikinci_hal_giris(self):
		self.hide()
		self.ikinci_hal_ac.show()
		self.ikinci_hal_ac.toolButton_back.clicked.connect(self.anasayfa_show)

	def ucuncu_hal_giris(self):
		self.hide()
		self.ucuncu_hal_ac.show()
		self.ucuncu_hal_ac.toolButton_back.clicked.connect(self.anasayfa_show)
		#self.ucuncu_hal_ac.hide()

			



