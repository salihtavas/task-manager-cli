from src.storage import JsonStorage
from src.task_manager import TaskManager


def show_menu():
    print("\nTask Manager CLI")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def main():
    storage = JsonStorage("data/tasks.json")
    manager = TaskManager(storage.load_tasks())

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task title: ")
            task = manager.add_task(title)
            storage.save_tasks(manager.list_tasks())
            print(f"Task added: {task.title}")

        elif choice == "2":
            tasks = manager.list_tasks()

            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "x" if task.completed else " "
                    print(f"[{status}] {task.id}. {task.title}")

        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                print("Invalid task ID.")
                continue

            if manager.complete_task(task_id):
                storage.save_tasks(manager.list_tasks())
                print("Task completed.")
            else:
                print("Task not found.")

        elif choice == "4":
            try:
                task_id = int(input("Task ID: "))
            except ValueError:
                print("Invalid task ID.")
                continue

            if manager.delete_task(task_id):
                storage.save_tasks(manager.list_tasks())
                print("Task deleted.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()