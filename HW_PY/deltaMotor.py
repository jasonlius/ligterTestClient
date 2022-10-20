import canopen
import time

def nodeConfig():
    network = canopen.Network()
    network.connect(bustype='slcan', channel='/dev/tty.usbmodem143101', bitrate=250000)
    deltaMotorNode = network.add_node(0x01,'/Users/mac/tmp/HW_PY/ASDA-A3_v04.eds')
    deltaMotorNode.nmt.state = 'OPERATIONAL'
    #docs https://hcrobots.feishu.cn/wiki/wikcnRos1XZ9nR1C5cXYaBgY1zd
    #p1-01 value is 0x010C
    deltaMotorNode.sdo[0x2101].write(0x010C)
    #p1-42 value is 0
    deltaMotorNode.sdo[0x212A].write(0x0)
    #p1-43 value is 0
    deltaMotorNode.sdo[0x212B].write(0x0)
    #p2-10 value is 0124
    deltaMotorNode.sdo[0x220A].write(0x0124)
    #p2-11 value is 0
    deltaMotorNode.sdo[0x220B].write(0x0)
    #p2-12 value is 0
    deltaMotorNode.sdo[0x220C].write(0x0)
    #p2-13 value is 0
    deltaMotorNode.sdo[0x220D].write(0x0)
    #p2-14 value is 0
    deltaMotorNode.sdo[0x220E].write(0x0)
    #p2-15 value is 0
    deltaMotorNode.sdo[0x220F].write(0x0)
    #p2-16 value is 0
    deltaMotorNode.sdo[0x2210].write(0x0)
    #p2-17 value is 0021
    # deltaMotorNode.sdo[0x2211].write(0x0021)
    #p2-18 value is 0
    deltaMotorNode.sdo[0x2212].write(0x0)
    #p2-19 value is 0
    deltaMotorNode.sdo[0x2213].write(0x0)
    #p2-20 value is 0108
    deltaMotorNode.sdo[0x2214].write(0x0108)
    #p2-21 value is 0
    deltaMotorNode.sdo[0x2215].write(0x0)
    #p2-22 value is 0
    deltaMotorNode.sdo[0x2216].write(0x0)
    #p3-00 value is 01(up)
    deltaMotorNode.sdo[0x2300].write(0x01)
    #p3-01 value is 0x0103 bitrate == 250000
    deltaMotorNode.sdo[0x2301].write(0x0103)
    print("node config finished!")

def deltaMotorTest():
    network = canopen.Network()
    network.connect(bustype='slcan', channel='/dev/tty.usbmodem143101', bitrate=250000)
    deltaMotorNode = network.add_node(1,'/Users/mac/tmp/HW_PY/ASDA-A3_v04.eds')
    deltaMotorNode.nmt.state = 'OPERATIONAL'
    deltaMotorNode.sdo[0x6040].write(0x00)
    deltaMotorNode.sdo[0x6040].write(0x80)
    deltaMotorNode.sdo[0x6040].write(0x00)
    deltaMotorNode.sdo[0x6060].write(0x01)
    deltaMotorNode.sdo[0x607A].write(-100000000)
    deltaMotorNode.sdo[0x6081].write(2000000)
    deltaMotorNode.sdo[0x6040].write(0)
    deltaMotorNode.sdo[0x6040].write(0x06)
    deltaMotorNode.sdo[0x6040].write(0x07)
    deltaMotorNode.sdo[0x6040].write(0x0f)
    deltaMotorNode.sdo[0x6040].write(0x2f)
    deltaMotorNode.sdo[0x6040].write(0x3f)
    deltaMotorNode.sdo[0x6040].write(0x2f)
    
     

if __name__ == "__main__":
    # nodeConfig()
    # print("please reboot your box during 10 seconds!")
    # time.sleep(10)
    deltaMotorTest()
    