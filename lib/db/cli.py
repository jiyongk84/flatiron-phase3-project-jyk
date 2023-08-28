from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Aircraft, Aircraft_Tasks
from simple_term_menu import TerminalMenu
from prettycli import blue

class AircraftTechApp:
    def __init__(self):
        # Create an SQLite database engine
        self.engine = create_engine("sqlite:///aircraft.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_aircraft_models(self):
        aircraft_list = self.session.query(Aircraft).all()
        models = [aircraft.model for aircraft in aircraft_list]
        return models

    def show_aircraft_models(self):
        aircraft_models = self.get_aircraft_models()
        aircraft_menu = TerminalMenu(aircraft_models)
        aircraft_entry_index = aircraft_menu.show()

        if aircraft_entry_index >= 0:
            selected_model = aircraft_models[aircraft_entry_index]
            print(f"You have selected aircraft model: {selected_model}")
            self.show_aircraft_tasks(selected_model)

    def show_aircraft_tasks(self, selected_model):
        tasks = self.session.query(Aircraft_Tasks).filter_by(ata_chapter_name=selected_model).all()
        if tasks:
            print("Tasks for selected aircraft model:")
            for task in tasks:
                print(f"ATA Chapter: {task.ata_chapter_number}, Task: {task.task}")
        else:
            print("No tasks available for selected aircraft model.")

    def main(self):
        print(blue("Welcome Aircraft tech! Please make a selection:"))
        options = ["Aircraft", "Pending work", "Quit"]
        menu = TerminalMenu(options)
        menu_entry_index = menu.show()

        if menu_entry_index == 0:  # Aircraft is selected
            self.show_aircraft_models()
        elif menu_entry_index == 1:  # Pending work is selected
            # Implement pending work logic here
            pass
        else:
            print("Goodbye!")

if __name__ == "__main__":
    app = AircraftTechApp()
    app.main()