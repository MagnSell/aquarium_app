import logging
import os
import uuid
import psycopg2
import psycopg2.extras
from dotenv import load_dotenv

def initialize_conn():
    # Load environment variables from .env file
    load_dotenv()

    db_url = os.getenv("DATABASE_URL")
    # Get database connection details from environment variables
    print("Trying to connect to the database")
    conn = psycopg2.connect(db_url, 
                                application_name="$ docs_simplecrud_psycopg2", 
                                cursor_factory=psycopg2.extras.RealDictCursor)
    print("Connected to the database")

    psycopg2.extras.register_uuid()
    return conn

def close_conn(conn):
    # Close communication with the database
    conn.close()
    print("Closed the connection to the database")

def create_tables(conn):
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create the Node_Measurement table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Node_Measurement (
            uuid UUID PRIMARY KEY,
            node_id INT,
            timestamp TIMESTAMP,
            temperature FLOAT,
            pH FLOAT,
            dissolved_oxygen FLOAT
        )
    """)

    # Create the Fish table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Fish (
            uuid UUID PRIMARY KEY,
            fish_id INT,
            timestamp TIMESTAMP,
            x_position FLOAT,
            y_position FLOAT,
            z_position FLOAT,
            x_velocity FLOAT,
            y_velocity FLOAT,
            z_velocity FLOAT
        )
    """)

    # Create the Control_Inputs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Control_Inputs (
            uuid UUID PRIMARY KEY,
            timestamp TIMESTAMP,
            heater BOOLEAN,
            light BOOLEAN,
            filter BOOLEAN,
            pump BOOLEAN
        )
    """)

    # Commit the changes to the database
    conn.commit()


def upsert_node_measurements(conn, node_measurements):
    # Create a cursor object to execute SQL queries
    print("Upserting node measurements")
    cursor = conn.cursor()

    # Upsert the Node_Measurements rows
    cursor.execute("""
        UPSERT INTO Node_Measurement (uuid, node_id, timestamp, temperature, pH, dissolved_oxygen)
        VALUES (%s, %s, %s, %s, %s, %s), (%s, %s, %s, %s, %s, %s)
    """, (node_measurements[0].uuid, node_measurements[0].node_id, node_measurements[0].timestamp,
          node_measurements[0].temperature, node_measurements[0].pH, node_measurements[0].dissolved_oxygen,
          node_measurements[1].uuid, node_measurements[1].node_id, node_measurements[1].timestamp,
          node_measurements[1].temperature, node_measurements[1].pH, node_measurements[1].dissolved_oxygen))

    # Commit the changes to the database
    conn.commit()
    print("Upserted node measurements")

def upsert_fish(conn, fish):
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Upsert the Fish row
    cursor.execute("""
        UPSERT INTO Fish (uuid, fish_id, timestamp, x_position, y_position, z_position, x_velocity, y_velocity, z_velocity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (fish.uuid, fish.fish_id, fish.timestamp, fish.x_position, fish.y_position,
          fish.z_position, fish.x_velocity, fish.y_velocity, fish.z_velocity))

    # Commit the changes to the database
    conn.commit()


def upsert_control_inputs(conn, control_inputs):
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Upsert the Control_Inputs row
    cursor.execute("""
        UPSERT INTO Control_Inputs (uuid, timestamp, heater, light, filter, pump)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (control_inputs.uuid, control_inputs.timestamp, control_inputs.heater,
          control_inputs.light, control_inputs.filter, control_inputs.pump))

    # Commit the changes to the database
    conn.commit()


def select_node_measurements(conn):
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Select all the Node_Measurement rows
    cursor.execute("SELECT * FROM Node_Measurement")

    # Fetch all the rows from the result
    rows = cursor.fetchall()

    # Commit the changes to the database
    conn.commit()

    return rows