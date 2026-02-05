from pydantic import BaseModel
from typing import List

class Passenger(BaseModel):
    name: str
    age: int
    gender: str
    berth: str

class BookingRequest(BaseModel):
    username: str
    password: str
    from_station: str
    to_station: str
    journey_date: str
    train_number: str
    class_name: str
    mobile: str
    passengers: List[Passenger] = []
