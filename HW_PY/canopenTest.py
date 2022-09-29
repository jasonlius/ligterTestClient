import random
import canopen
import pyttsx3
import time
def sayText(words):
    engine = pyttsx3.init()
    engine.setProperty('rate',200)
    engine.setProperty('volume',1.0)
    engine.setProperty('voice','com.apple.speech.synthesis.voice.tingting')
    engine.say(words)
    engine.runAndWait()
    engine.stop()

def findDevice(baud):
    isFindDevice = False
    network = canopen.Network()
    network.connect(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=baud)
    network.nmt.send_command(0x01)
    # This will attempt to read an SDO from nodes 1 - 127
    numbers = list(range(1,128))
    random.shuffle(numbers)
    sdo_req = b"\x40\x00\x10\x00\x00\x00\x00\x00"
    for node_id in numbers:
            network.send_message(0x600 + node_id, sdo_req)
    # We may need to wait a short while here to allow all nodes to respond
    time.sleep(0.05)
    for node_id in network.scanner.nodes:
        print("Found node %d!" % node_id)
        sayText(f"节点ID的为{node_id},16进制表示为{hex(node_id)}")
        isFindDevice = True
    network.disconnect()
    return isFindDevice

def searchBaud():
    isFindDevice = False
    while(isFindDevice == False):
        baudList = {100000,500000,250000,1000000,250000,50000,20000,125000}
        for baud in baudList:
            isFindDevice = findDevice(baud)
            if(isFindDevice == True):
                if(baud == 10000):
                    print("baud num is 1")
                    sayText(f"波特率ID为1")
                    return
                elif(baud == 20000):
                    print("baud num is 2")
                    sayText(f"波特率ID为2")
                    return
                elif(baud == 50000):
                    print("baud num is 3")
                    sayText(f"波特率ID为3")
                    return
                elif(baud == 100000):
                    print("baud num is 4")
                    sayText(f"波特率ID为4")
                    return
                elif(baud == 125000):
                    print("baud num is 5")
                    sayText(f"波特率ID为5")
                    return
                elif(baud == 250000):
                    print("baud num is 6")
                    sayText(f"波特率ID为6")
                    return
                elif(baud == 500000):
                    print("baud num is 7")
                    sayText(f"波特率ID为7")
                    return
                elif(baud == 1000000):
                    print("baud num is 8 or 0 other number ")
                    sayText(f"波特率ID为8或者0或者其他")
                    return
if __name__ == "__main__":
    searchBaud()