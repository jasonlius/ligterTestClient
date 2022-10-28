import sys
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainPage import Ui_MainWindow
from time import sleep



#####################################################
#                    创建主界面                       #
#####################################################
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.ser = None  # 串口初始化为None
        self.timer = QTimer(self)  # 实例化一个定时器
        self.timer.timeout.connect(self.refresh)  # 定时器结束后触发refresh
        self.timer.start(300)  # 开启定时器，间隔0.3s

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

    def configDriver(self):
        print("port change")

    def refresh(self):
        port_list = self.get_port_list()
        num = len(port_list)
        # print(num)
        num_last = self.serialcComboBox.count()
        # print(num_last)
        if (num != num_last):
            self.serialcComboBox.clear()
            self.serialcComboBox.addItems(self.get_port_list())   # 重新设置端口下拉列表

    @staticmethod
    # 获取端口号
    def get_port_list():
        """
        获取当前系统所有COM口
        :return:
        """
        com_list = []  # 用于保存端口名的列表
        port_list = serial.tools.list_ports.comports()  # 获取本机端口，返回list
        for port in port_list:
            com_list.append(port[0])  # 保存端口到列表
        return com_list  # 返回列表


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())