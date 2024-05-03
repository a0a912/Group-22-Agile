# This file contains the user authentication function and user database
# user databse is a list of dictionaries containing the username and password
users = [
    {
        "username": "admin",
        "password": "admin",
    },
    {
        "username": "ahmed",
        "password": "ahmed123",
    },
    {
        "username": "xinyu",
        "password": "xinyu123",
    },
    {
        "username": "eddie",
        "password": "eddie123",
    },
    {
        "username": "tom",
        "password": "tom123",
    },
    {
        "username": "ramu",
        "password": "ramu123",
    },
    {
        "username": "brandon",
        "password": "brandon123",
    },
]
# function to authenticate the user
def auth(username, password):
    for user in users:
        print(user["username"], user["password"])
        print(username, password)
        if user["username"] == username and user["password"] == password:
            return True
    return False