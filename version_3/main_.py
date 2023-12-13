from PyQt5.QtWidgets import QApplication
from Anasayfa__ import Anasayfa


app = QApplication([])
pencere = Anasayfa()
pencere.show()	

app.exec_()