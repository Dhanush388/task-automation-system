from datetime import datetime

def highlight_overdue(tasks):

    overdue = []

    for task in tasks:
        deadline = datetime.strptime(task[5], "%Y-%m-%d")

        if deadline < datetime.now() and task[7] != "Completed":
            overdue.append(task)

    return overdue


def suggest_priority(deadline):

    deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
    days_left = (deadline_date - datetime.now()).days

    if days_left <= 1:
        return "High"
    elif days_left <= 3:
        return "Medium"
    else:
        return "Low"
from datetime import datetime

def show_overdue(tasks):

    print("\n⚠ Overdue Tasks:")

    found = False

    for task in tasks:
        deadline = datetime.strptime(task[5], "%Y-%m-%d")

        if deadline < datetime.now() and task[7] != "Completed":
            print(task)
            found = True

    if not found:
        print("No overdue tasks!")
def suggest_priority(deadline):

    from datetime import datetime

    days = (datetime.strptime(deadline, "%Y-%m-%d") - datetime.now()).days

    if days <= 1:
        return "High"
    elif days <= 3:
        return "Medium"
    else:
        return "Low"