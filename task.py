import json

TASKS_FILE = 'tasks.json'
try:
    with open(TASKS_FILE, 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": "✅"})  
    save_tasks()


def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks")
        for idx, task in enumerate(tasks, 1):
            status = "[✅]" if task["completed"] == "✅" else "[ ]"
            print(f"{idx}. {status} {task['task']}")


def complete_task():
    view_tasks()
    choice = input("Enter the task number to mark as complete or type 'back' to return: ")

    if choice.lower() == 'back':
        return

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(tasks):
            if tasks[index]["completed"] == "✅":
                print(f'Task "{tasks[index]["task"]}" is already marked as complete.')
            else:
                tasks[index]["completed"] = "✅" 
                save_tasks()
                print(f'Task "{tasks[index]["task"]}" marked as complete!')
        else:
            print("Invalid task number.")
    else:
        print("Invalid input.")


def delete_task():
    view_tasks()
    task_number = input("Enter task number to delete or type 'back' to return: ")

    if task_number.lower() == 'back':
        return

    if task_number.isdigit():
        index = int(task_number) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)  # Remove task
            save_tasks()
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    else:
        print("Invalid input.")


def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def display_menu():
    print("===== Task Manager =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")
if __name__ == "__main__":
    main()
