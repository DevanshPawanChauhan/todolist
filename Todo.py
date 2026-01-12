def show_menu():
    print("1. Add task")
    print("2. View task")
    print("3. View task as done")
    print("4. Delete Task")
    print("4. Edit Task")
    print("6. Exit")

def add_task():
    task=input("enter a task")
    with open("task.txt","a") as file:
        file.write(task +"| PENDING\n")
    print("Task Added successfully")

def task_done():
    view_task()
    num=int(input("Enter the task to be marked done"))
    with open("task.txt","r") as file:
        task=file.readlines()
        task[num-1]=task[num-1].replace("PENDING","DONE")
        with open("task.txt", "w") as file:
         file.writelines(task)

    print("Task updated successfully!\n")

def del_task():
    view_task()
    num=int(input("Enter the task to be deleted"))
    with open("task.txt","r") as file:
        task=file.readlines()
        task.pop(num-1)
    with open("task.txt", "w") as file:
        file.writelines(task)

    print("Task deleted successfully!\n")

def edit_task():
    view_task()
    num=int(input("Enter the task to be changed"))
    with open("task.txt","r") as file:
        task=file.readlines()
        old_task=task[num-1].strip()
        print(f"{old_task}")
        new_task=input("Enter the new task")
        if " | " in task[num-1]:
            status=task[num-1].split("|")[1]
            task[num-1]=f"{new_task} |{status}"
        else:
            task[num-1]=new_task + "\n"
    with open("task.txt", "w") as file:
        file.writelines(task)

    print("Task updated successfully!\n")


def view_task():
    try:
        with open("task.txt",'r') as file:
            tasks=file.readlines()
            if not tasks:
                print("no task found")
            else:
                for i,task in enumerate(tasks,start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No file found")
while True:
    show_menu()
    choice=input("Enter a valid choice")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        task_done()
    elif choice=="4":
        del_task()
    elif choice=="5":
        edit_task()
    elif choice=="6":
        print("GoodBye")
        break
    else:
        print("enter a valid choice")