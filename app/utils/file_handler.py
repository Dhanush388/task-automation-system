import csv
import os
import json

def backup_tasks(tasks):

    with open("backup.json", "w") as f:
        json.dump(tasks, f)

    print("Backup created!")

def export_tasks(tasks):

    os.makedirs("exports", exist_ok=True)

    with open("exports/tasks.csv", "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            "ID","UserID","Title","Description",
            "Created","Deadline","Priority","Status"
        ])

        writer.writerows(tasks)

    print("Tasks exported successfully!")
def import_tasks(user_id):

    import csv
    from app.database.db import connect_db

    with open("exports/tasks.csv", "r") as f:

        reader = csv.reader(f)
        next(reader)

        conn = connect_db()
        cursor = conn.cursor()

        for row in reader:
            cursor.execute("""
            INSERT INTO tasks(user_id,title,description,created_date,deadline,priority,status)
            VALUES(?,?,?,?,?,?,?)
            """, (
                user_id,
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            ))

        conn.commit()
        conn.close()

    print("Tasks imported successfully!")