import os

FILENAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    print("\n📋 Your Tasks:")
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print()

def main():
    tasks = load_tasks()

    while True:
        print("To-Do List Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("✅ Task added!\n")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            task_num = int(input("Enter task number to mark as done: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                save_tasks(tasks)
                print("✔ Task marked as done!\n")
            else:
                print("❌ Invalid task number.\n")

        elif choice == "4":
            print("👋 Exiting... Tasks saved.")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
