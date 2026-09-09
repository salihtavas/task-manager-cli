from src.task_manager import TaskManager


def show_menu():
    print("\nTask Manager CLI")
    print("1. Add task")
    print("2. List tasks")
    print("3. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            task = manager.add_task(title)
            print(f"Task added: {task.title}")

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    print(f"{task.id}. {task.title}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()