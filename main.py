import arduino_communication as ac
import database_communication as dc
import time

def main():
    # Initialize the serial communication
    ser = ac.initialize_communication()
    conn = dc.initialize_conn()

    # Main Loop
    print("Hello World!")
    try:
        while True:
            # Receive data from the Arduino
            arduino_data = ac.receive_arduino_communication(ser)
            print(arduino_data)

            time.sleep(5)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the serial communication
        ac.close_communication(ser)
        dc.close_conn(conn)

if __name__ == "__main__":
    main()
