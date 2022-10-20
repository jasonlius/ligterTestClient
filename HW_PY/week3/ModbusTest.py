#!/usr/bin/env python3
from typing import IO
import minimalmodbus
import serial
instrument = minimalmodbus.Instrument('/dev/cu.usbserial-14330',0x01)  # port name, slave address (in decimal)
instrument.serial.baudrate = 38400
instrument.serial.bytesize = 8
instrument.serial.stopbits = 2
instrument.serial.parity   = serial.PARITY_NONE
instrument.mode = minimalmodbus.MODE_RTU
instrument.write_register(0x0102 ,0x10c,0,6)
instrument.write_register(0x030A ,0,0,6)
print(instrument.read_register(0x030A ,0,3))
instrument.serial.close()