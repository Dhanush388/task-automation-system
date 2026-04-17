import bcrypt
from app.database.db import connect_db

def register_user(username, password):

    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username,password) VALUES (?,?)",
            (username, hashed)
        )
        conn.commit()
        print("User registered successfully!")
    except:
        print("Username already exists!")

    conn.close()


def login_user(username, password):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id,password FROM users WHERE username=?",
        (username,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        user_id = result[0]
        hashed_password = result[1]

        if bcrypt.checkpw(password.encode(), hashed_password):
            print("Login successful!")
            return user_id

    print("Invalid credentials!")
    return None