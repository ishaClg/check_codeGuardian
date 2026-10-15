query = "SELECT * FROM users WHERE name = %s"
# later, when executing:
# cursor.execute(query, (username,))