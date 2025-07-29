import json

# Define the Task class
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed

    def mark_completed(self):
        self.completed = True

# Save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump([task.__dict__ for task in tasks], f)

# Load tasks from a JSON file
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return [Task(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

# Main menu logic
def main():
    tasks = load_tasks()
    while True:
        print("\n=== PERSONAL TO-DO LIST ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category: ")
            tasks.append(Task(title, description, category))
            print("✅ Task added!")

        elif choice == '2':
            if not tasks:
                print("📭 No tasks found.")
            else:
                for i, task in enumerate(tasks):
                    status = "✓" if task.completed else "✗"
                    print(f"\n{i+1}. [{status}] {task.title} ({task.category})")
                    print(f"    {task.description}")

        elif choice == '3':
            if not tasks:
                print("⚠️ No tasks to mark.")
            else:
                try:
                    idx = int(input("Enter task number to mark as completed: ")) - 1
                    if 0 <= idx < len(tasks):
                        tasks[idx].mark_completed()
                        print("✅ Task marked as completed.")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("⚠️ No tasks to delete.")
            else:
                try:
                    idx = int(input("Enter task number to delete: ")) - 1
                    if 0 <= idx < len(tasks):
                        deleted = tasks.pop(idx)
                        print(f"🗑️ Deleted task: {deleted.title}")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")

        elif choice == '5':
            save_tasks(tasks)
            print("💾 Tasks saved. Exiting...")
            break

        else:
            print("❌ Invalid option. Please choose 1 to 5.")

# ✅ FIXED: Correct entry point
if __name__ == "__main__":
    main()