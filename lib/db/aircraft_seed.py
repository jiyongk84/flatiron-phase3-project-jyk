from models import Aircraft
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///aircraft.db")
Session = sessionmaker(bind=engine)
session = Session()


import requests
import json

API_URL ="http://localhost:3000/aircraft"

response = requests.get(API_URL)
json_data = json.loads(response.text)

for aircraft_entry in json_data:
    aircraft = Aircraft(
        make=aircraft_entry["make"],
        model=aircraft_entry["model"],
        body_type=aircraft_entry["body_type"]
    )
    session.add(aircraft)
    session.commit()
