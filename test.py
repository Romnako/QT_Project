import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)            #create application
dlgMain = QWidget()                     #create main GUI window
#dlgMain = QMainWindow()                #более развернутый интерфейс GUI по сравнению с QWidget()
dlgMain.setWindowTitle('First GUI')
dlgMain.show()                          #show the GUI

app.exec_()                             #execute the app
