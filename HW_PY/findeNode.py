#!/usr/bin/env python
# coding=utf-8
import canopen
import time
import sys

network = canopen.Network()
network.connect(bustype='slcan', channel='/dev/cu.usbmodem143101', bitrate=250000)
max_node = 0x7F
list = []
def find_node():
    node_index = 1
    while (node_index < max_node):
        node = network.add_node(node_index, 'canio.eds')
        node.nmt.send_command(1)
        device_type = node.sdo['Device Type']
        try:
            print('node:',node_index,',data is:',device_type.raw)
        except:
            #print(node_index,'is not find')
            node_index = node_index + 1
            continue
        list.append(node_index)
        node_index = node_index + 1
    
find_node()
print('找到以下节点,十进制表示')
print(list)








