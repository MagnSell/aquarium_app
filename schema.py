from pydantic import BaseModel
from datetime import datetime


class Node_Measurement(BaseModel):
    uuid: float
    node_id: int
    timestamp: datetime
    temperature: float
    pH : float
    dissolved_oxygen: float


class Fish(BaseModel):
    uuid: float
    fish_id: int
    timestamp: datetime
    x_position: float
    y_position: float
    z_position: float
    x_velocity: float
    y_velocity: float
    z_velocity: float

class Control_Inputs(BaseModel):
    uuid: float
    timestamp: datetime
    heater: bool
    light: bool
    filter: bool
    pump: bool