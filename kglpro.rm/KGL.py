# Here we use a dictionary to store the username and password of the user.
# A dictionary allows you to store, retrieve and modify data efficiently.
# The if function checks for elements in a list and key/values in dictionries.
# The for function interrates over elements in a list and keys/values in dictionaries.

users = {"username" : "password"}

def register ():
    username = input("Enter username: ")

    if username in users:
        print("Username already exists")
        return
    
    password = input("Enter password:")
    users[username] = password
    print("user registered successfully")

register()


def login():
    print("login")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("invalid username or password")

login()




