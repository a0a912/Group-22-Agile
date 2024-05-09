
# this is a trial file for testing the update_score function

from user_crud_func import update_score, read_question_account

# you can register a new user and update the score, then change the user name or id to test the function
# update_score("ahmed", 100, ["1","2","3"], ["4","5","6"])
# update_score(2, 100, ["1","2","3"], ["4","5","6"])
# read_question_account(2) 


from usermod import select_id
select_id("QUESTION_BLANK", 2)
from model import select_word
select_word("QUESTION_DEFINITION", "apple")
from model import get_question_dict
get_question_dict("QUESTION_DEFINITION", "banana")