import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from serialPort import Ui_MainWindow


class MyWindow(QMainWindow, Ui_MainWindow):
    def __int__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


app = QApplication(sys.argv)
myWin = MyWindow()
myWin.show()
