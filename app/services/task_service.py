from app.database.db import connect_db
from datetime import datetime

def add_task(user_id, title, description, deadline, priority):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tasks(user_id,title,description,created_date,deadline,priority,status)
    VALUES(?,?,?,?,?,?,?)
    """, (
        user_id,
        title,
        description,
        datetime.now().strftime("%Y-%m-%d"),
        deadline,
        priority,
        "Pending"
    ))

    conn.commit()
    conn.close()

    print("Task added successfully!")


def view_tasks(user_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()

    conn.close()

    for t in tasks:
        print(t)

    return tasks


def complete_task(task_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE tasks SET status='Completed' WHERE id=?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    print("Task marked as completed!")


def delete_task(task_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    conn.commit()
    conn.close()

    print("Task deleted!")
def edit_task(task_id, title, description, deadline, priority):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE tasks
    SET title=?, description=?, deadline=?, priority=?
    WHERE id=?
    """, (title, description, deadline, priority, task_id))

    conn.commit()
    conn.close()

    print("Task updated successfully!")