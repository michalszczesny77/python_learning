class Task:
    def __init__(self, name):
        self.name = name


class TaskManager:

    def __init__(self):
        self.tasks = []

    def adding(self):
        new_task_name = input("Enter task name: ")
        new_task = Task(new_task_name)
        self.tasks.append(new_task)

    def removing(self):
        if not self.tasks:
            print("You have nothing to remove from the list!")
        else:
            while True:
                try:
                    number_to_remove = int(input("Enter a number of task: "))
                    if number_to_remove < 1:
                        print("Invalid Value")
                    else:
                        number_of_removed_task = number_to_remove - 1
                        removed_task = self.tasks.pop(number_of_removed_task)
                        print(f"[{removed_task.name.upper()}] task has been removed!")
                        break
                except (IndexError, ValueError):
                    print("Invalid Value")

    def showing(self):
        if not self.tasks:
            print("You have no tasks")
        else:
            print("\nYour tasks: ")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task.name}")

    def start(self):
        while True:
            try:
                print('''
                Task Manager 
1. Add task
2. Show tasks
3. Remove task
4. Exit
''')
                option = int(input("Enter your choice: "))
                if option == 1:
                    self.adding()
                elif option == 2:
                    self.showing()
                elif option == 3:
                    self.removing()
                elif option == 4:
                    print("Exiting...")
                    exit()
                else:
                    print("Invalid Value")
            except ValueError:
                print("Invalid Value!")


app = TaskManager()
app.start()