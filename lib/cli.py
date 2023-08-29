from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Aircraft, Aircraft_Tasks
from simple_term_menu import TerminalMenu
from prettycli import blue, red

class AircraftMaintApp:
    def __init__(self):
        self.engine = create_engine("sqlite:///aircraft.db")
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_aircraft_models(self):
        aircraft_list = self.session.query(Aircraft).all()
        models = [aircraft.model for aircraft in aircraft_list]
        return models

    def show_aircraft_models(self):
        while True:
            aircraft_models = self.get_aircraft_models()
            aircraft_menu = TerminalMenu(aircraft_models + ["Go Back"])
            aircraft_entry_index = aircraft_menu.show()

            if aircraft_entry_index >= 0 and aircraft_entry_index < len(aircraft_models):
                selected_model = aircraft_models[aircraft_entry_index]
                self.show_aircraft_tasks(selected_model)
            else:
                break

    def show_aircraft_tasks(self, selected_model):
        while True:
            print(blue(f"You have selected aircraft model: {selected_model}"))
            tasks = self.session.query(Aircraft_Tasks).all()

            if tasks:
                task_strings = [f"ATA {task.ata_chapter_number}, {task.task}" for task in tasks]
                task_menu = TerminalMenu(task_strings + ["Go Back"], title="Select a Task:")
                task_index = task_menu.show()

                if task_index >= 0 and task_index < len(tasks):
                    selected_task = tasks[task_index]
                    print(red(f"You selected: ATA {selected_task.ata_chapter_number} : {selected_task.task}"))
                else:
                    break
            else:
                print("No tasks available for selected aircraft model.")
                break

    def main(self):
        while True:
            print(blue("Welcome Aircraft Tech! Please make a selection:"))
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
                break

if __name__ == "__main__":
    app = AircraftMaintApp()
    app.main()
