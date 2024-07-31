import json
import os
from datetime import datetime

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

# Function to validate date
def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to add a task
def add_task(tasks, description, priority, due_date):
    if priority not in ['high', 'medium', 'low']:
        print("Invalid priority. Please choose from 'high', 'medium', or 'low'.")
        return

    if not validate_date(due_date):
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

# Function to remove a task
def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    removed_task = tasks.pop(index)
    save_tasks(tasks)
    print(f"Task removed: {removed_task['description']}")

# Function to mark a task as completed
def complete_task(tasks, index):
    if index < 0 or index >= len(tasks):
        print("Invalid task number.")
        return
    tasks[index]['completed'] = True
    save_tasks(tasks)
    print(f"Task marked as completed: {tasks[index]['description']}")

# Function to display tasks
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i + 1}. {task['description']} (Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status})")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            priority = input("Enter task priority (high, medium, low): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, description, priority, due_date)
        elif choice == '2':
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                remove_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '3':
            try:
                index = int(input("Enter the task number to mark as completed: ")) - 1
                complete_task(tasks, index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            display_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
