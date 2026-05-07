import sqlite3

DB_PATH = "data/users.db"


def get_user_by_id(user_id: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    result = cursor.execute(query).fetchall()

    conn.close()
    return result


def list_users(role: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if role == "admin":
        query = "SELECT * FROM users"
    else:
        query = f"SELECT * FROM users WHERE role = '{role}'"

    result = cursor.execute(query).fetchall()

    conn.close()
    return result