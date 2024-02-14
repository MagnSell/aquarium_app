import arduino_communication as ac
import database_communication as dc


def main():
    # Initialize the serial communication
    ser = ac.initialize_communication()
    conn = dc.initialize_conn()
    print("Hello World!")

    # Close the serial communication
    ac.close_communication(ser)
    dc.close_conn(conn)

if __name__ == "__main__":
    main()
