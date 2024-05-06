from usermod import execute, drop, select, update, create, select_username, select_id,select_all, delete
import sqlite3
database = './database/database.db'
# connect to the database
connection = sqlite3.connect(database,check_same_thread=False) # create the file if it does not exist 
cursor = connection.cursor() # cursor is used to interact with the database 
print("Connected to database")

############################################################################################
# test adding one new user to the database                                                 #
# arguments for create() is table_name, column_name, value                                 #                 
# ACCOUNT table has columns: id, username, password, role, score                           #  
# eg, create("account", "username,password,role,score", "'ahmed','ahmed123','user',0")     #
############################################################################################
# create("account", "username,password,role,score", "'xinyu','xinyu123','user',0")

############################################################################################
# select one user through username                                                    #
# arguments for select_username() is username                                              #
# e.g select_username("admin")                                                             # 
############################################################################################          
# select_username("admin")  

############################################################################################
# updating the score of a user                                                        #
# arguments for update() is table_name, column_name, value, condition                      #
# condition should be in the format of "column_name=value" like "id=1" or "username=xxx"   #
# statement = "UPDATE {table_name} SET {column_name} = {value} WHERE {condition}"          #
# e.g update("account", "password", 'admin123', "username=admin")                                                      #
# e.g update("account", "score", 200,"id=1")                                               #
############################################################################################
# update("account", "password", "admin124","id=1")  # update the password of the user with id 1
# select_username("admin") # check if the password has been updated

############################################################################################
# selecting a user through id                                                              #
# arguments for select_id() is table_name, id, [column]                                    #
# e.g select_id("account",1,"*")                                                           #
# e.g select_id("account",1)                                                               #
############################################################################################
# select_id("account",1)

############################################################################################
# deleting a user from the database                                                        #
# arguments for delete() is table_name, condition                                          #
# condition should be in the format of "column_name=value" like "id=1" or "username=xxx"   #
# e.g delete("account", "id=1")                                                            #
############################################################################################
# delete("account", "id=2") # delete the user with id 2
# delete("account", "username=xinyu") # delete the user with username xinyu

############################################################################################
# selecting all users from the database                                                    #
# arguments for select_all() is table_name                                                 #
# e.g select_all("account")                                                                #
############################################################################################
# select_all("account")


############################################################################################
# authorizing a user                                                                       #
# arguments for auth() is username, password                                               #
# if the user is authenticated, return True, "Authenticated"                               #
# if the user is not authenticated, return False, "User not found"                         #
# if the user is found but the password is incorrect, return False, "Password incorrect"   #
# auth("ahmed", "ahmed123")                                                                #
############################################################################################
def auth(username, password) -> tuple: 
    # return a tuple, tuple[0] is the boolean, tuple[1] is the information
    statement_auth="SELECT Username,Password FROM account"
    rows = cursor.execute(statement_auth)
    # print(rows)
    result = rows.fetchall()
    print(result)
    for row in result:
        if row[0] == username and row[1] == password:
            print(f"User {row[0]} authenticated")
            return True, "Authenticated"
        elif row[0] == username and row[1] != password:
            print(f"User {row[0]} Password incorrect")
            return False, "Password incorrect"
    print(f"User {username} not found")
    return False, "User not found"

############################################################################################
# signing up a new user                                                                    #
# arguments for sign_up() is username, password                                            #
# if the user already exists, return False, "User already exists"                          #
# if the user does not exist, create the user and return True, "User created"              #
# sign_up("ahmed", "ahmed123")                                                             #
############################################################################################
def sign_up(username, password) -> tuple: # return a tuple, tuple[0] is the boolean, tuple[1] is the information
    users = select_all("account", "username")
    # print(users)
    for user in users:
        if user[0] == username:
            print(f"User {username} already exists")
            return False, "User already exists"
    create("account", "username,password,role,score", f"'{username}','{password}','user',0")
    return True, "User created"

def update_score(index, score) -> tuple: # return a tuple, tuple[0] is the boolean, tuple[1] is the information
    if not isinstance(score, int):
        return False, "Score should be an integer"
    if isinstance(index, int):
        col = "id"
        old_score = select_id("account", index, "score")[0]
    else:
        old_score = select_username(index, "score")[0]
        col = "username"
    score += old_score
    print("the old score is", old_score)
    print("the new score is", score)
    update("account", "score", score, f"{col}='{index}'")
    return True, "Score updated"
    
"""
how to build functions for the following functionalities:
1. Forget password

"""
