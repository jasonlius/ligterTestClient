import can
def receive_all(baud):
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""
    bus1 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=10000)    
    # bus2 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=500000)  
    # bus3 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=1000000)    
    # bus4 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=50000)    
    # bus5 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=125000)    
    # bus6 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=20000)    
    # bus7 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=100000)    
    bus8 = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem143201', bitrate=250000)  


    k=1
    for bus in [bus1,bus8]:
        print("receiving date now ...... ")
        print(f"BUS{k} start!")
        try:
            for i in range(0,4):
                msg = bus.recv(1)
                print(bus)
                if msg is not None:
                    print(msg)
            i+=1
        except KeyboardInterrupt:
            pass  # exit normally


if __name__ == "__main__":
    receive_all(500000)