from usermod import execute, drop, select, update, create, select_username, select_id,select_all, delete,insert
import sqlite3
database = './database/database.db'
# connect to the database
connection = sqlite3.connect(database,check_same_thread=False) # create the file if it does not exist 
cursor = connection.cursor() # cursor is used to interact with the database 
print("Connected to database")

############################################################################################
# adding one new user to the database                                                 #
# arguments for create() is table_name, column_name, value                                 #                 
# ACCOUNT table has columns: id, username, password, role, score                           #  
# eg, create("account", "username,password,role,score", "'ahmed','ahmed123','user',0")     #
# the called function above equals to the following SQL statement                          #
# "INSERT INTO ACCOUNT(username,password,role,score) VALUES ('ahmed','ahmed123','user',0)" #
# please note that the value should be in the format of "'value1','value2','value3',value4"#
# pay attention to the single quotes around the values                                     #
############################################################################################

############################################################################################
# select one user through username                                                         #
# arguments for select_username() is username                                              #
# e.g select_username("admin")                                                             #
# the called function above equals to the following SQL statement                          #
# "SELECT * FROM account WHERE username = 'admin'"                                         # 
############################################################################################          

############################################################################################
# updating the score of a user                                                             #
# arguments for update() is table_name, column_name, value, condition                      #
# condition should be in the format of "column_name=value" like "id=1" or "username=xxx"   #
# statement = "UPDATE {table_name} SET {column_name} = {value} WHERE {condition}"          #
# e.g update("account", "password", 'admin123', "username=admin")                          #
# the called function above equals to the following SQL statement                          #
# "UPDATE account SET password = admin123 WHERE username=admin"                            #
# e.g update("account", "score", 200,"id=1")                                               #
# the called function above equals to the following SQL statement                          #
# "UPDATE account SET score = 200 WHERE id=1"                                              #
############################################################################################

############################################################################################
# selecting a user through id                                                              #
# arguments for select_id() is table_name, id, [column]                                    #
# e.g select_id("account",1,"score")                                                       #
# the called function above equals to the following SQL statement                          #
# "SELECT score FROM account WHERE id=1"                                                   #
# e.g select_id("account",1)                                                               #
# the called function above equals to the following SQL statement                          #
# "SELECT * FROM account WHERE id=1"                                                       #
# it returns a tuple of the information of the user                                        #
# it can also be used to get info from other tables                                        #
# e.g select_id("QUESTION_ACCOUNT",1)                                                      #
# e.g select_id("QUESTION_BLANK",1,"word")                                                 #
############################################################################################

############################################################################################
# deleting a user from the database                                                        #
# arguments for delete() is table_name, condition                                          #
# condition should be in the format of "column_name=value" like "id=1" or "username=xxx"   #
# e.g delete("account", "id=1")                                                            #
# the called function above equals to the following SQL statement                          #
# "DELETE FROM account WHERE id=1"                                                         #
# e.g delete("account", "username=xinyu")                                                  #
# the called function above equals to the following SQL statement                          #
# "DELETE FROM account WHERE username=xinyu"                                               #
############################################################################################
 
############################################################################################
# selecting all users from the database                                                    #
# arguments for select_all() is table_name                                                 #
# e.g select_all("account")                                                                #
# the called function above equals to the following SQL statement                          #
# "SELECT * FROM account"                                                                  #
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
# The called function above equals to the following SQL statement                          #
# "INSERT INTO ACCOUNT(username,password,role,score) VALUES ('ahmed','ahmed123','user',0)" #
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

############################################################################################
# updating the score of a user                                                             #
# arguments for update_score() is index, score, correct_questions, incorrect_questions     #
# correct_questions and incorrect_questions are lists of questions                         #
# questions list should be in the format of ["question_id","question_id","question3_id"]   #
# question list can be empty                                                               #
# index can be the id of the user or the username of the user                              #
# e.g update_score(1, 100, ["1","2","3"], ["4","5","6"])                                   #
# e.g update_score("ahmed", 100, ["1","2","3"], ["4","5","6"])                             #
# The called function above equals to the following SQL statement                          #
# "INSERT INTO QUESTION_ACCOUNT(id,correct_questions,incorrect_questions) VALUES {100, ["1","2","3"], ["4","5","6"]}" 
# if the user is found, update the score and the correct and incorrect questions           #
# return True, "Score updated, correct and incorrect questions updated"                    #
# if the score is not an integer, return False, "Score should be an integer"               #
############################################################################################
def update_score(index, score,correct_questions:list=None,incorrect_questions:list=None) -> tuple: # return a tuple, tuple[0] is the boolean, tuple[1] is the information
    if not isinstance(score, int):
        return False, "Score should be an integer"
    if isinstance(index, int):
        account_id=index
        try:
            old_score = select_id("account", account_id, "score")[0]
        except:
            print(f"User {index} not found")
            return False, "User not found"
    else:
        try:
            old_score = select_username(index, "score")[0]
            account_id = select_username(index, "id")[0]
        except:
            print(f"User {index} not found")
            return False, "User not found"
    score += old_score
    print("the old score is", old_score)
    print("the new score is", score)
    # update the score of the user with the new score in the ACCOUNT table of database
    update("ACCOUNT", "score", score, f"id='{account_id}'")
    # if there is nothing in the list, set it to empty list
    if not correct_questions:
        correct_questions = []
    if not incorrect_questions:
        incorrect_questions = []
    correct_questions = list(set(correct_questions)) # remove duplicates
    incorrect_questions = list(set(incorrect_questions)) # remove duplicates
    # update the correct and incorrect questions of the user in the QUESTION_ACCOUNT table of database
    # the correct and incorrect questions are stored as a string in the database
    value = f'({account_id},"{correct_questions}","{incorrect_questions}")' 
    table_name = "QUESTION_ACCOUNT"
    column_name = "account_id,correct_questions,incorrect_questions"
    insert(table_name,column_name,value)
    return True, "Score updated, correct and incorrect questions updated"

#update_score("xinyu", 100, ["1","2","3"], ["4","5","6"])
############################################################################################
# reading all data about one user from the QUESTION_ACCOUNT table using user_id            #
# arguments for read_question_account() is user_id                                         #
# e.g read_question_account(1)                                                             #
# The called function above equals to the following SQL statement                          #
# "SELECT * FROM QUESTION_ACCOUNT, ACCOUNT WHERE QUESTION_ACCOUNT.account_id = ACCOUNT.id AND ACCOUNT.id=1" #
# return the username, correct questions and incorrect questions of the user               #
# in a dictionary format                                                                   #
# e.g {"username":"ahmed","correct_questions":["1","2","3"],"incorrect_questions":["4","5","6"]} #
############################################################################################
def read_question_account(id:int) -> dict:
    statement = f"SELECT * FROM QUESTION_ACCOUNT, ACCOUNT WHERE QUESTION_ACCOUNT.account_id = ACCOUNT.id AND ACCOUNT.id={id}"
    rows = cursor.execute(statement)
    result = rows.fetchall()
    correct_list=[]
    incorrect_list=[]
    # get all the information of the user under the condition
    for i in result:
        [qa_id, account_id, correct_questions, incorrect_questions, account_id, username, password, role, score] = i
        # get the correct and incorrect questions of the user of each record and add them to the list
        correct_list+=eval(correct_questions)
        incorrect_list+=eval(incorrect_questions)
    # remove duplicates
    correct_list=list(set(correct_list)) 
    incorrect_list=list(set(incorrect_list))
    # build a dictionary for the user
    user_dict = {"username":username,"correct_questions":correct_list,"incorrect_questions":incorrect_list}
    print(user_dict)
    return user_dict


"""
how to build functions for the following functionalities:

document my functions about how to use them.
you can tell me where you need clarification.
1. CRUD for questions
    1.Update questions
    2.delete questions
3. Forget password
4. Admin dashboard(delete user)
5. rank func

"""
