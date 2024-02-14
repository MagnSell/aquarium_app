import arduino_communication as ard_com
import database_communication as db_com
import schema

def main():
    conn = db_com.initialize_communication()
    ser = ard_com.initialize_communication()
    print("Hello World")
    ard_com.close_communication(ser)
    db_com.close_communication(conn)

if __name__ == "main":
    main()
