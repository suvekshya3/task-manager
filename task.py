import json

tasks_manager = "tasks.json"

def add_tasks():
    try:
        file = open(tasks_manager, "r") 
        tasks = json.load(file)
        file.close()
        return tasks 
    except (FileNotFoundError , json.JSONDecodeError):
            return()

import json

def save_tasks(tasks):
    try:
        file = open("tasks_manager.json", "w")
        json.dump(tasks, file, indent=4)
        file.close()
        print("Tasks have been saved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_task():
    task = input("Enter task: ")
    tasks = add_tasks()
    if task in [t["task"] for t in tasks]:
        print("Task already exists!")
        return
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added!")

def view_tasks():
    tasks = add_tasks()
    if not tasks:
        print("No tasks found!")
    for i, t in enumerate(tasks):
        status = "Done" if t["completed"] else "Not Done"
        print(f"{i+1}. {t['task']} - {status}")

def complete_task():
    tasks = add_tasks()
    view_tasks()
    try:
        num = int(input("Enter task number to complete: ")) - 1
        tasks[num]["completed"] = True
        save_tasks(tasks)
        print("Task marked as complete!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def delete_task():
    tasks = add_tasks()
    view_tasks()
    try:
        num = int(input("Enter task number to delete: ")) - 1
        del tasks[num]
        save_tasks(tasks)
        print("Task deleted!")
    except (IndexError, ValueError):
        print("Invalid task number!")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
