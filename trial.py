
# this is a trial file for testing the update_score function

from user_crud_func import update_score, read_question_account, sign_up
from usermod import insert_secure_question, show_secure_question, check_secure_question
# you can register a new user and update the score, then change the user name or id to test the function
# update_score("ahmed", 100, ["1","2","3"], ["4","5","6"])
# update_score(2, 100, ["1","2","3"], ["4","5","6"])
# read_question_account(2) 


# from usermod import select_id
# select_id("QUESTION_BLANK", 2)
# from model import select_word
# select_word("QUESTION_DEFINITION", "apple")
# from model import get_question_dict
# get_question_dict("QUESTION_DEFINITION", "banana")
# sign_up("xinyu", "xinyu1234")

# username = "xinyu"
# secure_question1 = "What is your favorite color?"
# answer1 = "red"
# secure_question2 = "What is your favorite food?"
# answer2 = "pizza"
# insert_secure_question(username, secure_question1,answer1, secure_question2,answer2)

show_secure_question("xinyu")
# print(check_secure_question("xinyu", ["What is your favorite color?","What is your favorite food?"], ["red","pizza"]))
# print(check_secure_question("xinyu", ["What is your favorite color?","What is your favorite food?"], ["blue","pizza"]))
# print(check_secure_question("xinyu", ["What is your favorite?","What is your favorite food?"], ["red","pizza"]))
# print(check_secure_question("xinyu", ["What is your favorite color?","What is your favorite food?"], ["blue","apple"]))

