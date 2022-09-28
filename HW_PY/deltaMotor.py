import canopen

def function1():
    network = canopen.Network()
    network.connect(bustype='slcan', channel='/dev/tty.usbmodem143301', bitrate=250000)
    deltaMotorNode = network.add_node(2,'/Users/mac/tmp/HW_PY/ASDA-A3_v04.eds')
    deltaMotorNode.sdo.download(0x2101, 0, b'\x0d\x01')
    infile = deltaMotorNode.sdo.upload(0x2101, 0)
    # Open a file for writing to
    outfile = open('out.eds', 'w', encoding='ascii')
    # Iteratively read lines from node and write to file
    outfile.writelines(str(infile))
    # Clean-up

if __name__ == "__main__":
    function1()