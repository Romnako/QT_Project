import sys
from PyQt5.QtWidgets import *

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Second GUI')                      # add wigets, set properties
        self.resize(300, 200)                                  # size of GUI window

        self.ledText = QLineEdit('Default text', self)
        self.ledText.move(90, 50)                             # move window of wiget

        self.btnUpdate = QPushButton('Update Window title', self)
        self.btnUpdate.move(95, 90)
        self.btnUpdate.clicked.connect(self.evt_btn_update_clicked)


    def evt_btn_update_clicked(self):
        self.setWindowTitle(self.ledText.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)                               # create application
    dlgMain = DlgMain()                                        # create main GUI window
    dlgMain.show()                                             # show GUI
    sys.exit(app.exec_())                                      # execute the application
