import arduino_communication as ac
import database_communication as dc
import time

def main():
    REFRESH_RATE = 5
    # Initialize the serial communication
    ser = ac.initialize_communication()
    conn = dc.initialize_conn()

    # Create the tables in the database if they don't exist
    #dc.create_tables(conn)

    # Main Loop
    try:
        while True:
            # Receive data from the Arduino
            arduino_data = ac.receive_arduino_communication(ser)
            node_measurements = ac.convert_arduino_data_to_node_measurements(arduino_data)
            print(node_measurements)

            # Upsert the Node_Measurement rows
            if node_measurements:
                dc.upsert_node_measurements(conn, node_measurements)
            
            # Print the Node_Measurement rows
            #print(dc.select_node_measurements(conn))
                
            time.sleep(REFRESH_RATE)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the serial communication
        ac.close_communication(ser)
        dc.close_conn(conn)

if __name__ == "__main__":
    main()
