import pandas as pd
import matplotlib.pyplot as plt

def show_analytics(tasks):

    if not tasks:
        print("No tasks available")
        return

    df = pd.DataFrame(tasks, columns=[
        "id","user_id","title","desc",
        "created","deadline","priority","status"
    ])

    print("\nTask Summary:")
    print(df["status"].value_counts())

    df["status"].value_counts().plot(kind="bar")

    plt.title("Task Completion Stats")
    plt.xlabel("Status")
    plt.ylabel("Count")

    plt.show()
def completion_percentage(tasks):

    total = len(tasks)

    if total == 0:
        print("No tasks available")
        return

    completed = sum(1 for t in tasks if t[7] == "Completed")

    percent = (completed / total) * 100

    print(f"Completion: {percent:.2f}%")
# 🔹 Tasks per week
def tasks_per_week(tasks):

    import pandas as pd

    if not tasks:
        print("No tasks available")
        return

    df = pd.DataFrame(tasks, columns=[
        "id","user_id","title","desc",
        "created","deadline","priority","status"
    ])

    df["created"] = pd.to_datetime(df["created"])

    weekly = df.groupby(df["created"].dt.isocalendar().week).size()

    print("\nTasks per week:")
    print(weekly)


# 🔹 Pending vs Completed
def task_ratio(tasks):

    if not tasks:
        print("No tasks available")
        return

    pending = sum(1 for t in tasks if t[7] == "Pending")
    completed = sum(1 for t in tasks if t[7] == "Completed")

    print(f"\nPending: {pending}, Completed: {completed}")