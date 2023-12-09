from PyQt5.QtWidgets import QApplication
from anasayfa_python import Anasayfa

app = QApplication([])
pencere = Anasayfa()
pencere.show()	
app.exec_()