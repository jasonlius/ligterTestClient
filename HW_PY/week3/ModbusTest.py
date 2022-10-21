#!/usr/bin/env python3
from typing import IO
import minimalmodbus
import serial
#modBus协议基本串口参数配置
instrument = minimalmodbus.Instrument('/dev/cu.usbserial-14330',0x7f)  # port name, slave address (in decimal)
instrument.serial.baudrate = 38400
instrument.serial.bytesize = 8
instrument.serial.stopbits = 2
instrument.serial.parity   = serial.PARITY_NONE
instrument.mode = minimalmodbus.MODE_RTU

#P1-01参数
#标准CANOpen，需要根据提升机现场实际运行方向进行调整，配置值为0x000C或0x010C。向上提升方向为正。
instrument.write_register(0x0102 ,0x10c,0,6)
#P2-10参数 备注DI1
instrument.write_register(0x0214 ,0x0124,0,6)
#P2-11参数 备注DI2
instrument.write_register(0x0216 ,0x0,0,6)
#P2-12参数 备注DI3
instrument.write_register(0x0218 ,0x0,0,6)
#P2-13参数 备注DI4
instrument.write_register(0x021A ,0x0,0,6)
#P2-14参数 备注DI5
instrument.write_register(0x021C ,0x0,0,6)
#P2-15参数 备注DI6
instrument.write_register(0x021E ,0x0,0,6)
#P2-16参数 备注DI7
instrument.write_register(0x0220 ,0x0,0,6)
#P2-17参数 备注DI8只用于加保护传感器 默认值x21，测试值0
instrument.write_register(0x0222 ,0x0,0,6)
#P2-18参数 备注Do1
instrument.write_register(0x0224 ,0x0,0,6)
#P2-19参数 备注Do2
instrument.write_register(0x0226 ,0x0,0,6)
#P2-20参数 备注Do3
instrument.write_register(0x0228 ,0x108,0,6)
#P2-21参数 备注Do4
instrument.write_register(0x022A ,0x0,0,6)
#P2-22参数 备注Do5
instrument.write_register(0x022C ,0x0,0,6)
#P3-00参数 备注CANOpen node ID，上升列为1，下降列为2
instrument.write_register(0x0300 ,0x1,0,6)
#P3-01参数 备注CANOpen 波特率CAN bus 250 Kbps
instrument.write_register(0x0302 ,0x0103,0,6)

instrument.serial.close()