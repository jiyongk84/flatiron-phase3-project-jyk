from models.aircraft_models import Aircraft_Tasks
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("sqlite:///aircraft.db")
Session = sessionmaker(bind=engine)
session = Session()


import requests
import json

API_URL = "http://localhost:3001/aircraft_tasks"

response = requests.get(API_URL)
json_data = json.loads(response.text)

for task_entry in json_data:
    task = Aircraft_Tasks(
        ata_chapter_number=task_entry["ata_chapter_number"],
        ata_chapter_name=task_entry["ata_chapter_name"],
        task=task_entry["task"]
    )
    session.add(task)
    session.commit()
