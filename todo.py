
import json

class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task Completed\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            desc = input("Description: ")
            cat = input("Category: ")
            tasks.append(Task(title, desc, cat))

        elif choice == '2':
            for i, task in enumerate(tasks):
                status = "✓" if task.completed else "✗"
                print(f"{i+1}. [{status}] {task.title} - {task.category}\n   {task.description}")

        elif choice == '3':
            idx = int(input("Task number to mark complete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks[idx].mark_completed()

        elif choice == '4':
            idx = int(input("Task number to delete: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)

        elif choice == '5':
            save_tasks(tasks)
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
