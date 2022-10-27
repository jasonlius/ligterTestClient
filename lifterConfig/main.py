import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication
from serialAPP import Ui_MainWindow



########################
#函数区
####################################################
# 串口函数区
def getPortList():
    Com_List = []
    plist = list(serial.tools.list_ports.comports())
    if len(plist) > 0:
        for i in range(len(plist)):
            Com_List.append(list(plist[i])[0])
    print(Com_List)
    return Com_List

#####################################################
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
portList = getPortList()
if portList!=[]:
    for i in range(len(portList)):
        myWin.comboBox.addItem(portList[i])
    serialPort = portList[0]
else:
    serialPort = None
    myWin.show_dialog(str='请先打开串口')
sys.exit(app.exec_())