# Backend for application
- Receives sensor data from Arduino in JSON format
- Sends to database in CockroachDB

# How to use
- Clone repository and create virtual environment with Python 3.8 and requirements.txt
- Create .env file with DATABASE_URL
- Create logs folder for storing logged data.
- Run main.py

## Known issues
- Sometimes the Arduino doesn't send anything and will get a print message "Received b'' from Arduino". If this persists for more than once or twice restart program until voltage information gets sendt.
- Sensor data always arrives after two lines of information about voltage from Arduino.
