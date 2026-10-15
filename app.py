username = input("Enter username: ")

query = "SELECT * FROM users WHERE name = %s"
cursor.execute(query, (username,))

print(query)
print("hello world")
print("Bava")
print("Ani")

