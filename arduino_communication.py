import serial
import time
import json
import pandas as pd
import datetime
import csv

def initialize_communication():
    # Create a serial object
    ser = serial.Serial()

    # Set the port and baud rate
    ser.port = '/dev/ttyUSB0'
    ser.baudrate = 115200

    # Set the timeout for receiving data (in seconds)
    ser.timeout = 1

    # Open the serial connection
    ser.open()

    # Check if the serial connection is open
    if ser.is_open:
        print("Serial connection established.")
    else:
        print("Failed to establish serial connection.")
    return ser


def close_communication(ser):
    ser.close()

def arduino_communication():
    ser = initialize_communication()
    first = True
    while True:
        data = ser.readline()  # Read a line of data

        time_stamp = datetime.datetime.now()
        try:

            json_data = json.loads(data)
            # Print the received data
            print("Received data:", json_data)
            # Create a DataFrame from the received data
            print(first)
            if first:
                df = pd.DataFrame()
                for key, value in json_data.items():
                    for i in range(len(value)):
                        df[key + "_" + str(i)] = [value[i]]

                df["time"]=time_stamp
                df.to_csv("data.csv",index=False)

                first = False
            else:
                with open('data.csv', 'a', newline='') as file:
                    writer = csv.writer(file)

                    # Append the values to their corresponding rows
                    row = []
                    for key, values in json_data.items():
                        row.extend(values)

                    row.append(time_stamp)
                    writer.writerow(row)

        except KeyboardInterrupt as e:
            print("Received keyboard interrupt, closeing serial port ")
            ser.close()
        except json.decoder.JSONDecodeError as e:
            print("Failed to parse the received data: ", data)
        except Exception as e:
            print(f"Unexpected error on data: {data}, error: {type(e)}")
        finally:
            time.sleep(5)  # Wait for 5 second
