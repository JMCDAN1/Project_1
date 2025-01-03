print("hello, user")
task = []

def menu():
    while True:
        choice = input("1. add task - 2. view task - 3. delete task - 4. quit the application")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("exiting application, Thank you!")
            break
        else:
            print("invalid input")
    


def add_task():
    task = input("enter the task you would like to add: ")
    task.append(task)
    print(f"task {task} is added")
    

def view_task():
    for i in task:
        print(i)



def delete_task():
    if task:
        try:
            task_index = int(input("Enter the task number to delete: "))
            if 1 <= task_index <= len(task):
                removed_task = task.pop(task_index - 1)
                print(f"Task '{removed_task}' task deleted.")
            else:
                print("Error: Invalid task number.")
        except ValueError:
            print("Error: Please enter a valid number.")
    else:
        print("No tasks to delete.")

menu()