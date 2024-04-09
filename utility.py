import uuid
from datetime import datetime
from schema import Node_Measurement
import pandas as pd

def convert_sensor_data_to_dataframe(data):
    # Create a Node_Measurement object
    node_measurements = []
    node_id = 0
    for _, sensor in data.items():
        node_measurement = Node_Measurement(
            uuid = uuid.uuid4(),
            timestamp = datetime.now(),
            node_id=node_id,
            temperature=sensor["temperature"],
            pH=sensor["pH"],
            dissolved_oxygen=sensor["dissolved_oxygen"]
        )
        node_measurements.append(node_measurement)
        node_id += 1

    # Create a dataframe from the node measurements
    df = pd.DataFrame([nm.__dict__ for nm in node_measurements])
    return df