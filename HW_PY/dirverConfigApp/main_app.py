import sys
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainPage import Ui_MainWindow


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

    def changePort(self):
        global PortNumber
        PortNumber = self.serialcComboBox.currentText()
        print(f"{PortNumber} has been changed!")

    def changenodeId(self):
        print("port change")

    def ProtectSensor(self):
        print("port change")

    def detectBaud(self):
        print("port change")

    def detectNodeId(self):
        print("port change")



app = QApplication(sys.argv)
myWin = MyWindow()
myWin.show()
portList = getPortList()
if portList!=[]:
    for i in range(len(portList)):
        myWin.serialcComboBox.addItem(portList[i])
    serialPort = portList[0]
else:
    serialPort = None
    myWin.show_dialog(str='请先打开串口')
sys.exit(app.exec_())