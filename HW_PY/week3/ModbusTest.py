#!/usr/bin/env python3
import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/cu.usbserial-14310',0x01)  # port name, slave address (in decimal)
instrument.serial.baudrate = 38400
## Read temperature (PV = ProcessValue) ##
f = instrument.read_register(18 ,2,3)  
print(f)