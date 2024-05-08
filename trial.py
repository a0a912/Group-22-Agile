
# this is a trial file for testing the update_score function

from user_crud_func import update_score, read_question_account
# you can register a new user and update the score, then change the user name or id to test the function
update_score("admin", 100, ["1","2","3"], ["4","5","6"])
update_score(1, 100, ["1","2","3"], ["4","5","6"])
read_question_account(1) 