# To-Do List Application

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print(f"Task '{task}' added!")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter task number to remove: ")) - 1
            removed = tasks.pop(index)
            print(f"Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("Invalid task number!")


def main():
    tasks = []

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

main()
