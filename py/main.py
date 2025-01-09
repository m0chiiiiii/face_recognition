import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QIcon
from mainWindow import Ui_mainWindow
from scanFace_v2 import scanFace
from registerWindow import  registerWindow


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(r'C:\Users\Mariel\Documents\CTU 3rd Yr (1st Sem)\ITHC\Face Recognition\py\fc-logo (45x40).png'))

        #open scan face window
        self.scanFaceBtn.clicked.connect(self.openScanner)

        #open register window
        self.registerBtn.clicked.connect(self.openRegister)

    #function to open scan face window 
    def openScanner(self):
        self.hide()
        self.camWindow = scanFace(self)
        self.camWindow.setWindowIcon(QIcon(r'C:\Users\Mariel\Documents\CTU 3rd Yr (1st Sem)\ITHC\Face Recognition\py\fc-logo (45x40).png'))
        self.camWindow.show()


    #function to open register window 
    def openRegister(self):
        self.hide()
        self.regWindow = registerWindow(self)
        self.regWindow.setWindowIcon(QIcon(r'C:\Users\Mariel\Documents\CTU 3rd Yr (1st Sem)\ITHC\Face Recognition\py\fc-logo (45x40).png'))
        self.regWindow.show()

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

