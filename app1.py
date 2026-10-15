
import sqlite3

def get_user(username):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Intentionally vulnerable: SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    print("hello world")

    return cursor.fetchall()
