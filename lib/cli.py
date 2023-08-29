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
        self.pending_tasks = []

    #Retrieves the aircraft models in aircraft.db
    def get_aircraft_models(self):
        aircraft_list = self.session.query(Aircraft).all()
        models = [aircraft.model for aircraft in aircraft_list]
        return models

    #Display the aircraft models as menu items
    def show_aircraft_models(self):
        while True:
            aircraft_models = self.get_aircraft_models()
            aircraft_menu = TerminalMenu(aircraft_models + ["Go Back"])
            aircraft_entry_index = aircraft_menu.show()
    #Conditions after task selection
            if aircraft_entry_index >= 0 and aircraft_entry_index < len(aircraft_models):
                selected_model = aircraft_models[aircraft_entry_index]
                self.handle_aircraft_tasks(selected_model)
            else:
                break

    

    #Initial app menu
    def main(self):
        while True:
            print(blue("Welcome Aircraft Tech! Please make a selection:"))
            options = ["Aircraft", "Pending work", "Quit"]
            menu = TerminalMenu(options)
            menu_entry_index = menu.show()
            # Aircraft is selected
            if menu_entry_index == 0:  
                self.show_aircraft_models()
            # Pending work is selected
            elif menu_entry_index == 1:  
                self.manage_pending_work()
        
            else:
                if self.pending_tasks:
                    print("You have pending tasks. Are you sure you want to quit? (Y/N)")
                    choice = input().lower()
                    if choice == 'y':
                        print("Goodbye!")
                        break
                else:
                    print("Goodbye!")
                    break

if __name__ == "__main__":
    app = AircraftMaintApp()
    app.main()
