import json
import os

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    print("\n" + "=" * 35)
    print("         YOUR TO-DO LIST")
    print("=" * 35)
    if not tasks:
        print("  No tasks yet! Add one below.")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else "○"
        print(f"  {i}. [{status}] {task['title']}")
    print("=" * 35 + "\n")

def add_task(tasks):
    title = input("Enter task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Added: '{title}'")
    else:
        print("Task cannot be empty!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"Marked '{tasks[num-1]['title']}' as done!")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a number!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: '{removed['title']}'")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a number!")

def menu():
    print("\n1. View tasks")
    print("2. Add task")
    print("3. Mark complete")
    print("4. Delete task")
    print("5. Quit")
    return input("\nChoose an option (1-5): ")

def main():
    print("\nWelcome to your To-Do List!")
    tasks = load_tasks()
    while True:
        choice = menu()
        if choice == "1": show_tasks(tasks)
        elif choice == "2": add_task(tasks)
        elif choice == "3": complete_task(tasks)
        elif choice == "4": delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

main()