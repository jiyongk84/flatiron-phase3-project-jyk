from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Aircraft, Aircraft_Tasks
from simple_term_menu import TerminalMenu
from prettycli import blue, red, yellow, green, magenta
from helpers import App_Heading

heading = App_Heading()



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

    #Display aircraft tasks from aircraft.db as menu items
    def handle_aircraft_tasks(self, selected_model):
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
                    self.pending_tasks.append(selected_task)
                    print("Task added to pending work.")
                else:
                    break
            else:
                print("No tasks available for selected aircraft model.")
                break
    #Adding tasks to pending bucket
    def add_task_to_pending(self):
        print(red("Do you want to add an existing task or a new task?"))
        options = ["Existing Task", "New Task", "Cancel"]
        menu = TerminalMenu(options, title="Add Task:")
        option_index = menu.show()
        #Display all the tasks from aircraft database as selectable by suer
        if option_index == 0: 
            tasks = self.session.query(Aircraft_Tasks).all()

            if tasks:
                task_strings = [f"ATA {task.ata_chapter_number}, {task.task}" for task in tasks]
                task_menu = TerminalMenu(task_strings + ["Go Back"], title="Select an Existing Task:")
                task_index = task_menu.show()

                if task_index >= 0 and task_index < len(tasks):
                    selected_task = tasks[task_index]
                    self.pending_tasks.append(selected_task)
                    print("Existing task added to pending work.")
                else:
                    print("No existing tasks available.")
            else:
                print("No existing tasks available.")
        #Input fields for adding new tasks not including in the database
        elif option_index == 1:
            print("Add a new task to pending work:")
            ata_chapter_number = input("Enter the ATA chapter number: ")
            ata_chapter_name = input("Enter ATA name: ")
            task_description = input("Enter the task description: ")

            
        #Check if all input fields have information.
            if not ata_chapter_number or not ata_chapter_name or not task_description:
                print(yellow("ATA chapter number and task description cannot be empty. Task addition cancelled."))
            else:       
                new_task = Aircraft_Tasks(ata_chapter_number=ata_chapter_number, ata_chapter_name=ata_chapter_name, task=task_description)
                self.pending_tasks.append(new_task)
                self.session.add(new_task)
                self.session.commit()
                print("New task added to pending work.")

        else:
            print("Task addition cancelled.")

    #Delete added task from database
    def remove_task_from_database(self, task):
        self.session.delete(task)
        self.session.commit()
    
    #Handle Pending work tasks
    def manage_pending_work(self):
        while True:
            if not self.pending_tasks:
                print(red("No pending tasks."))
            else:
                print("Pending tasks:")
                for i, task in enumerate(self.pending_tasks, start=1):
                    print(f"{i}. ATA {task.ata_chapter_number} : {task.task}")
            #Pending tasks submenu
            options = ["Add Task", "Remove Task", "Go Back"]
            menu = TerminalMenu(options, title="Pending Work:")
            option_index = menu.show()

            if option_index == 0:
                self.add_task_to_pending()
            elif option_index == 1:
                if not self.pending_tasks:
                    print("No pending tasks to remove.")
                else:
                    task_strings = [f"ATA {task.ata_chapter_number}, {task.task}" for task in self.pending_tasks]
                    task_menu = TerminalMenu(task_strings + ["Go Back"], title="Select a Task to Remove:")
                    task_index = task_menu.show()

                    if task_index >= 0 and task_index < len(self.pending_tasks):
                        removed_task = self.pending_tasks.pop(task_index)
                        print(f"Task removed from pending work: ATA {removed_task.ata_chapter_number} : {removed_task.task}")
                        self.remove_task_from_database(removed_task)  # Remove the task from the database
            else:
                break

    #Initial app menu
    def main(self):
        while True:
            heading.hello_air_tech()
            print(green("Welcome Aircraft Tech! Please make a selection:"))
            options = ["Aircraft", "Pending work", "Quit"]
            menu = TerminalMenu(options)
            menu_entry_index = menu.show()
            # Aircraft is selected
            if menu_entry_index == 0:  
                self.show_aircraft_models()
            # Pending work is selected
            elif menu_entry_index == 1:  
                self.manage_pending_work()

            #Check if any pending tasks before exiting the app
            else:
                if self.pending_tasks:
                    print(yellow("You have pending tasks. Are you sure you want to quit? (Y/N)"))
                    choice = input().lower()
                    if choice == 'y':
                        print(magenta("Goodbye!"))
                        break
                else:
                    print(magenta("Goodbye!"))
                    break

if __name__ == "__main__":
    app = AircraftMaintApp()
    app.main()
