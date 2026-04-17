from app.services.auth_service import register_user, login_user
from app.services.task_service import add_task, view_tasks, complete_task, delete_task
from app.services.analytics_service import show_analytics
from app.utils.file_handler import export_tasks


def start_app():

    user_id = None

    while True:

        print("\n==== Task Automation System ====")
        print("1 Register")
        print("2 Login")
        print("3 Add Task")
        print("4 View Tasks")
        print("5 Complete Task")
        print("6 Delete Task")
        print("7 Analytics")
        print("8 Export CSV")
        print("9 Exit")
        print("10 Edit Task")
        print("11 Show Overdue Tasks")
        print("12 Import CSV")

        choice = input("Select option: ")

        if choice == "1":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            register_user(username, password)

        elif choice == "2":
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            user_id = login_user(username, password)

        elif choice == "3":
            if not user_id:
                print("Please login first!")
                continue

            title = input("Title: ")
            desc = input("Description: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            priority = input("Priority (Low/Medium/High): ")

            add_task(user_id, title, desc, deadline, priority)

        elif choice == "4":
            if user_id:
                view_tasks(user_id)
            else:
                print("Login first!")

        elif choice == "5":
            task_id = int(input("Task ID: "))
            complete_task(task_id)

        elif choice == "6":
            task_id = int(input("Task ID: "))
            delete_task(task_id)

        elif choice == "7":


            if not user_id:


                print("Please login first!")
                continue

            from app.services.analytics_service import (
                show_analytics,
                completion_percentage,
                tasks_per_week,
                task_ratio
            )

            tasks = view_tasks(user_id)

            show_analytics(tasks)
            completion_percentage(tasks)
            tasks_per_week(tasks)
            task_ratio(tasks)

        elif choice == "8":
            if user_id:
                tasks = view_tasks(user_id)
                export_tasks(tasks)
            else:
                print("Login first!")

        elif choice == "9":
            print("Goodbye!")
            

        elif choice == "10":
           
           task_id = int(input("Task ID: "))
           title = input("New Title: ")
           desc = input("New Description: ")
           deadline = input("New Deadline (YYYY-MM-DD): ")
           priority = input("New Priority: ")

           from app.services.task_service import edit_task
           edit_task(task_id, title, desc, deadline, priority)
        elif choice == "11":

            
            from app.services.automation_service import show_overdue
            tasks = view_tasks(user_id)
            show_overdue(tasks) 
            
        elif choice == "12":

            from app.utils.file_handler import import_tasks
            import_tasks(user_id)
            break

        else:
            print("Invalid option!")