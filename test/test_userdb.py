import manage,database,user_crud_func
import unittest
def test_return_all_secure_question():
    # get all the secure questions from the database
    secure_questions = manage.return_all_secure_question()
    print("All secure questions are:")
    # check if the secure questions are the same as the secure questions in the secure_question_list
    assert secure_questions == database.secure_question_list.secure_questions
    print("All secure questions are the same")
    # return secure_questions
# def test_check_secure_question():
#     user_crud_func.sign_up("eddie", "eddie123", "What is your favorite color?",'red',"What is your favorite food?","pizza")
#     assert user_crud_func.check_secure_question("eddie", ["What is your favorite color?","What is your favorite food?"], ["red","pizza"]) == True
#     assert user_crud_func.check_secure_question("eddie", ["What is your favorite color?","What is your favorite food?"], ["blue","pizza"]) == False
#     assert user_crud_func.check_secure_question("eddie", ["What is your favorite?","What is your favorite food?"], ["red","pizza"]) == False

# def test_show_secure_question():
#     user_crud_func.sign_up("eddie", "eddie123", "What is your favorite color?",'red',"What is your favorite food?","pizza")
#     assert user_crud_func.show_secure_question("eddie") == ["What is your favorite color?", "What is your favorite food?"]