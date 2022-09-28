import can
def receive_all():
    """Receives all messages and prints them to the console until Ctrl+C is pressed."""
    with can.interface.Bus(
        bustype='slcan', channel='/dev/tty.usbmodem143301', bitrate=250000
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
    receive_all()