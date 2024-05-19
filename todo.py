import os

class TaskManager:
    def __init__(self, filename='tasks.txt'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks = [line.strip() for line in file.readlines()]
        else:
            tasks = []
        return tasks

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task}\n")

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1] = new_task
            self.save_tasks()
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks.pop(task_number - 1)
            self.save_tasks()
        else:
            print("Invalid task number.")

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List Application")
        print("1. View tasks")
        print("2. Add task")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.view_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            manager.add_task(task)
            print("Task added.")
        elif choice == '3':
            manager.view_tasks()
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter new task: ")
            manager.update_task(task_number, new_task)
            print("Task updated.")
        elif choice == '4':
            manager.view_tasks()
            task_number = int(input("Enter task number to delete: "))
            manager.delete_task(task_number)
            print("Task deleted.")
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
