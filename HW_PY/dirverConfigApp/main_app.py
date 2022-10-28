import sys

import canopen as canopen
import minimalmodbus as minimalmodbus
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow, QApplication
from mainPage import Ui_MainWindow
from time import sleep

#####################################################
#                    功能函数区                       #
#####################################################

#配置根据公司给出的参数表配置台达电机
def configDeltaMotor(portNumber):
    try:
        # modBus协议基本串口参数配置
        mainUI.textBrowser.append("初始化连接串口")
        instrument = minimalmodbus.Instrument(portNumber, 0x7f)  # port name, slave address (in decimal)
        instrument.serial.baudrate = 38400
        instrument.serial.bytesize = 8
        instrument.serial.stopbits = 2
        instrument.serial.parity = serial.PARITY_NONE
        instrument.mode = minimalmodbus.MODE_RTU
    except Exception:
        mainUI.textBrowser.append("初始化串口失败，请检查连线是否已经插牢，或者串口是否选择错误")

    try:
        mainUI.textBrowser.append("开始配置参数")
        # P1-01参数
        # 标准CANOpen，需要根据提升机现场实际运行方向进行调整，配置值为0x000C或0x010C。向上提升方向为正。
        instrument.write_register(0x0102, 0x10c, 0, 6)
        # P2-10参数 备注DI1
        instrument.write_register(0x0214, 0x0124, 0, 6)
        # P2-11参数 备注DI2
        instrument.write_register(0x0216, 0x0, 0, 6)
        # P2-12参数 备注DI3
        instrument.write_register(0x0218, 0x0, 0, 6)
        # P2-13参数 备注DI4
        instrument.write_register(0x021A, 0x0, 0, 6)
        # P2-14参数 备注DI5
        instrument.write_register(0x021C, 0x0, 0, 6)
        # P2-15参数 备注DI6
        instrument.write_register(0x021E, 0x0, 0, 6)
        # P2-16参数 备注DI7
        instrument.write_register(0x0220, 0x0, 0, 6)
        # P2-17参数 备注DI8只用于加保护传感器 默认值0x21，测试值0
        instrument.write_register(0x0222, SensorValue, 0, 6)
        # P2-18参数 备注Do1
        instrument.write_register(0x0224, 0x0, 0, 6)
        # P2-19参数 备注Do2
        instrument.write_register(0x0226, 0x0, 0, 6)
        # P2-20参数 备注Do3
        instrument.write_register(0x0228, 0x108, 0, 6)
        # P2-21参数 备注Do4
        instrument.write_register(0x022A, 0x0, 0, 6)
        # P2-22参数 备注Do5
        instrument.write_register(0x022C, 0x0, 0, 6)
        # P3-00参数 备注CANOpen node ID，上升列为1，下降列为2
        instrument.write_register(0x0300, NodeID, 0, 6)
        # P3-01参数 备注CANOpen 波特率CAN bus 250 Kbps
        instrument.write_register(0x0302, 0x0103, 0, 6)
        instrument.serial.close()
        mainUI.textBrowser.append("驱动器参数配置成功")
    except Exception:
        mainUI.textBrowser.append("参数配置失败，请重试")

def testLifter(portNumber):
    try:
        mainUI.textBrowser.append("开始测试提升机电机运转")
        network = canopen.Network()
        network.connect(bustype='slcan', channel=portNumber, bitrate=250000)
        deltaMotorNode = network.add_node(1, './ASDA-A3_v04.eds')
        deltaMotorNode.nmt.state = 'OPERATIONAL'
        deltaMotorNode.sdo[0x6040].write(0x00)
        deltaMotorNode.sdo[0x6040].write(0x80)
        deltaMotorNode.sdo[0x6040].write(0x00)
        deltaMotorNode.sdo[0x6060].write(0x01)
        deltaMotorNode.sdo[0x607A].write(100000000)
        deltaMotorNode.sdo[0x6081].write(4000000)
        deltaMotorNode.sdo[0x6040].write(0)
        deltaMotorNode.sdo[0x6040].write(0x06)
        deltaMotorNode.sdo[0x6040].write(0x07)
        deltaMotorNode.sdo[0x6040].write(0x0f)
        deltaMotorNode.sdo[0x6040].write(0x2f)
        deltaMotorNode.sdo[0x6040].write(0x3f)
        deltaMotorNode.sdo[0x6040].write(0x2f)
        mainUI.textBrowser.append("提升机测试运转成功")
    except Exception:
        mainUI.textBrowser.append("提升机测试失败，请检查以下几点")
        mainUI.textBrowser.append("1：驱动器参数是否选择正确，2：驱动器配置完成是否重启，3：canopen连线是否正确")

#####################################################
#                    创建主界面                       #
#####################################################
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        global mainUI
        super(MyWindow, self).__init__(parent)
        mainUI = self
        self.setupUi(self)
        self.ser = None  # 串口初始化为None
        self.timer = QTimer(self)  # 实例化一个定时器
        self.timer.timeout.connect(self.refresh)  # 定时器结束后触发refresh
        self.timer.start(300)  # 开启定时器，间隔0.3s
        self.setFont(QFont('Helvetica Neue'))
    def changePort(self):
        global PortNumber
        PortNumber = self.serialcComboBox.currentText()
        self.textBrowser.setPlainText(f"切换到串口 {PortNumber}")

    def changenodeId(self):
        global NodeID
        if self.canopenIdComboBox.currentText() == "1(上升列)":
            NodeID = 0x1
        else:
            NodeID = 0x2
        self.textBrowser.append(f"canopenID为{NodeID}")
    def ProtectSensor(self):
        global SensorValue
        if self.SensorDetectcomboBox.currentText() == "加保护":
            SensorValue = 0x21
        else:
            SensorValue = 0x0
        self.textBrowser.append(f"传感器参数配置值为{SensorValue}")

    def detectBaud(self):
        print("port change")

    def detectNodeId(self):
        print("port change")

    def configDriver(self):
        configDeltaMotor(PortNumber)

    def testLifter(self):
        testLifter(PortNumber)

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