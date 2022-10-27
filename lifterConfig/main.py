import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from serialAPP import Ui_MainWindow
#创建主界面
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

    def portChange(self):
        print("port change")

    def baudChange(self):
        print("port change")

    def sendBtn(self):
        print("port change")

    def connectBtn(self):
        print("port change")


app = QApplication(sys.argv)
myWin = MyWindow()
myWin.show()
sys.exit(app.exec_())