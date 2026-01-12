def show_menu():
    print("1. Add task")
    print("2. View task")
    print("3. Exit")
while True:
    show_menu()
    choice=input("Enter a valid choiice")

    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        print("GoodBye")
        break
    else:
        print("enter a valid choice")