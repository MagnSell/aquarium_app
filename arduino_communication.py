import serial
import json
import uuid
from datetime import datetime
from schema import Node_Measurement

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
    print("Serial connection closed.")

def receive_arduino_communication(ser):
    data = ser.readline()  # Read a line of data
    json_data = {}
    try:
        json_data = json.loads(data)
    except json.decoder.JSONDecodeError as e:
        print("Failed to parse the received data: ", data)
    except Exception as e:
        print(f"Unexpected error on data: {data}, error: {type(e)}")
    finally:
        return json_data