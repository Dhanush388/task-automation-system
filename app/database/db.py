import sqlite3
import os

DB_PATH = "data/tasks.db"

def connect_db():
    return sqlite3.connect(DB_PATH)

def create_tables():
    os.makedirs("data", exist_ok=True)

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        description TEXT,
        created_date TEXT,
        deadline TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()