
import canopen
import can


def sendDate():
    
    id = int(input("Enter can ID : ") , base=16)

    n = int(input("Enter number of data elements : "))
    # Below line read inputs from user using map() function 
    Can_data = list(map(lambda x:int(x,16),input("\nEnter the numbers : ").strip().split()))[:n]

    bus_send = can.interface.Bus(bustype='slcan', channel='/dev/cu.usbmodem141101', bitrate=250000)
    msg = can.Message(arbitration_id=id,
                    data=Can_data,
                    is_extended_id=False)
    print(msg)
    try:
        bus_send.send(msg)
        print("Message sent on {}".format(bus_send.channel_info))
    except can.CanError:
        print("Message NOT sent")

def receive_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""
    with can.interface.Bus(
        bustype='slcan', channel='/dev/cu.usbmodem141101', bitrate=250000
    ) as bus:
        
        print("receiving date now ...... ")
        try:
            while True:
                msg = bus.recv(1)
                if msg is not None:
                    print(msg)

        except KeyboardInterrupt:
            pass  # exit normally


if __name__ == "__main__":
    sendDate()
