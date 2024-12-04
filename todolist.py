class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Enter Task Title: ")
        description = input("Enter Task Description: ")
        task = Task(title, description)
        self.tasks.append(task)
        print("Task added Successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No Tasks Available!")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task.completed else "Not Completed"
                print(f"{i}. {task.title} - {status}")

    def update_task(self):
        if not self.tasks:
            print("No tasks available!")
        else:
            self.view_tasks()
            task_number = int(input("Enter the task number to Update: "))
            if task_number > 0 and task_number <= len(self.tasks):
                task = self.tasks[task_number - 1]
                print("1. Update Title")
                print("2. Update Description")
                choice = input("Enter Your Choice: ")
                if choice == "1":
                    task.title = input("Enter New Title: ")
                elif choice == "2":
                    task.description = input("Enter New Description: ")
                print("Task Updated Successfully!")
            else:
                print("Invalid Task Number!")

    def delete_task(self):
        if not self.tasks:
            print("No Tasks Available!")
        else:
            self.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            if task_number > 0 and task_number <= len(self.tasks):
                del self.tasks[task_number - 1]
                print("Task Deleted Successfully!")
            else:
                print("Invalid Task Number!")

    def mark_as_completed(self):
        if not self.tasks:
            print("No Tasks Available!")
        else:
            self.view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            if task_number > 0 and task_number <= len(self.tasks):
                self.tasks[task_number - 1].completed = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark as completed")
        print("6. Exit")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            todo_list.mark_as_completed()
        elif choice == "6":
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
