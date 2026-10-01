username = input("Enter username: ")

query = "SELECT * FROM users WHERE name = '" + username + "'"

print(query)

# New change for webhook test
password = input("Enter password: ")
login_query = "SELECT * FROM users WHERE password = '" + password + "'"

print(login_query)
