# This file contains the user authentication function and user database
# user databse is a list of dictionaries containing the username and password
users = [
    {
        "username": "admin",
        "password": "admin",
        "role":"admin",
        "score": 0,
        "wrong_question":[]
    },
    {
        "username": "ahmed",
        "password": "ahmed123",
        "role":"user",
        "score": 0,
        "wrong_question":[]
    },
    {
        "username": "xinyu",
        "password": "xinyu123",
        "role":"user",
        "score": 0,
        "wrong_question":[]
    },
    {
        "username": "eddie",
        "password": "eddie123",
        "role":"user",
        "score": 0,
        "wrong_question":[]
    },
    {
        "username": "tom",
        "password": "tom123",
        "role":"user",
        "score": 0,
        "wrong_question":[]
    },
    {
        "username": "ramu",
        "password": "ramu123",
        "role":"user",
        "score": 0,
        "wrong_question":[]
    },
    {
        "username": "brandon",
        "password": "brandon123",
        "role":"user",
        "score": 0,
        "wrong_question":[]
    },
]
# function to authenticate the user
def auth(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True
    return False

def sign_up(username, password):
    for user in users:
        if user["username"] == username:
            return False
    users.append({
        "username": username,
        "password": password,
        "role": "user",
        "score": 0,
        "wrong_question": []
    })
    return True