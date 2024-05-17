# a simple login page using flask for testing the usermod.py
from flask import Flask, render_template, url_for, request, redirect, session, flash
from model import Word, get_question_dict
from user_crud_func import auth, sign_up, select_all, show_secure_question,update
from usermod import execute, select_all, update, check_secure_question
from manage import return_all_secure_question
import secrets 
import json
app = Flask(__name__)
app.secret_key = "d4413d05138d1fa03489e233df6aca24"

# page of login when you open the website 127.0.0.1:8888/

@app.route('/', methods=['GET'])
def home():
    username = session.get('username')
    return render_template("home.html", username=username)

@app.route('/login', methods=['GET'])
def login_page():
    username = session.get('username')
    return render_template("login.html", username=username)

@app.route('/register', methods=['GET'])
def register_page():
    list_of_secure_questions = return_all_secure_question()
    return render_template("register.html", list_of_secure_questions=list_of_secure_questions)

@app.route('/forgot', methods=['GET'])
def forgot_page():
    return render_template("forgot.html")


# login route making a post request to the server to check the username and password using the auth function from usermod.py
@app.route('/auth/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # print(username, password)
    result = auth(username, password)
    

    if result[0]:
        session['username'] = username
        # if the user is authenticated then redirect to the home page with the username
        return redirect(url_for('home'))
    else:
        # if the user is not authenticated then redirect to the login page with a message
        session['fail_count'] = session.get('fail_count', 0) + 1
        # if the user tried 5 times then redirect to the login page with a message
        if 3 <= session.get('fail_count') < 5:
            attempts = session.get('fail_count')
            message = f"You tried {attempts} attempts. You have only {5 - attempts} more attempts."
            flash(message)
            
        if session.get('fail_count') == 5:
            message = "You tried 5 attempts. Please try again later."
            flash(message)
            
        return redirect(url_for('login_page'))

# register route making a post request to the server to check the username and password using the sign_up function from usermod.py
@app.route('/auth/register', methods=['POST'])
def register():
    
    username = request.form.get('username')
    password = request.form.get('password')
    secure_question1 = request.form.get('secure_question1')
    secure_question2 = request.form.get('secure_question2')
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')

    # if the two questions are same, then redirect to the register page with an error message
    if secure_question1 == secure_question2:
        flash('The two security questions must be different.', 'error')
        return redirect(url_for('register_page'))
    
    result = sign_up(username, password, secure_question1, answer1, secure_question2, answer2)
    if result[0]:
        return redirect(url_for('login_page'))

# making a post request to the server to check the username and password 
@app.route('/auth/forgot', methods=['POST'])
def forgot():
    list_of_secure_questions = return_all_secure_question()
    username = request.form.get('username')
    secure_question1 = request.form.get('secure_question1')
    secure_question2 = request.form.get('secure_question2')
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')
    new_password = request.form.get('new_password')

    # if the two answers in database and the input answers matches, then update the password
    if check_secure_question(username, [secure_question1, secure_question2], [answer1, answer2]):
        update(username,"password", new_password, f"username='{username}'")
        return redirect(url_for('login_page'), list_of_secure_questions=list_of_secure_questions)
    else:
        session['fail_count'] = session.get('fail_count', 0) + 1
        if 3 <= session.get('fail_count') < 5:
            attempts = session.get('fail_count')
            message = f"You tried {attempts} attempts. You have only {5 - attempts} more attempts."
        if session.get('fail_count') == 5:
            message = "You tried 5 attempts. Please try again later."
        return message

# making a post request to the server to get secure questions
@app.route('/get_secure_questions', methods=['POST'])
def get_secure_questions():
    username = request.form.get('username')
    secure_questions = show_secure_question(username)
    return redirect(url_for('forgot_page'), secure_questions=secure_questions)

# logout route to remove the username from the session
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/ranking', methods=['GET'])
def ranking():
    scores = select_all("account", "username, score")
    #Sort the scores in descending order
    scores.sort(key=lambda x: x[1], reverse=True)
    return render_template("scores.html", scores=scores)

# profile route to show the profile of the user
@app.route('/profile', methods=['GET'])
def profile():
    username =session.get('username')
    return render_template("profile.html", username=username)

# update the password of the user in the profile page
@app.route('/profile/update/password', methods=['POST'])
def update_password():
    username = session.get('username')
    password = request.form.get('password')
    new_password = request.form.get('new_password')
    # check if the current password is correct
    current_password = select_all("account", "password", f"username='{username}'")
    if password == current_password:
        update("account", "password", new_password, f"username='{username}'")
    else:
        # if the current password is incorrect, then redirect to the profile page with a message
        flash("The current password is incorrect")

    return redirect(url_for('profile')) 

@app.route('/question')
def question():
    # random number from 1-14, cant be 0
    num = 0 
    while num == 0:
 
        num = secrets.randbelow(14)

    #get the questions from the database
    questions = get_question_dict("QUESTION_BLANK", num)
    questions = questions['example']

    incorrect = get_question_dict("QUESTION_BLANK", num)
    incorrect = incorrect['incorrect_list']

    correct  = get_question_dict("QUESTION_BLANK", num)
    #correct = correct['correct']
    

    # Parse the JSON string
    # incorrect_list = json.loads(incorrect)

    # # Access the elements of the list
    # choice1 = incorrect_list[0]
    # choice2 = incorrect_list[1]
    # choice3 = incorrect_list[2]

    correct = correct['correct']
    print(correct)
    questions_list = []
    questions_id = []
    for i in range(10):
            num = 0
            while num == 0:
                num = secrets.randbelow(14)
                questions_id.append(num)
                if num in questions_id:
                    continue 

            question_data = get_question_dict("QUESTION_BLANK", num)

            question_dict = {
            'question': question_data.get('example'),
            'incorrect_list': json.loads(question_data.get('incorrect_list')),
            'id': question_data.get('id'),
            'correct': question_data.get('correct')
        }

            questions_list.append(question_dict)
            questions_list_json = json.dumps(questions_list)

    print(len(questions_list))
                


    questions_list_json = json.dumps(questions_list)


    return render_template("question.html", questions_list=questions_list_json)



#Test for test_db_data.html
@app.route('/test_db_data')
def test_db_data():
    username = session.get('username')
    #Get blank questions from database
    question_blank = select_all("QUESTION_BLANK")

    #Get defination questions from database
    question_defination = select_all("QUESTION_DEFINITION")

    # Convert the fetched data into JSON strings
    question_blank_json = json.dumps(question_blank)
    question_definition_json = json.dumps(question_defination)
    
    return render_template("test_db_data.html", question_blank=question_blank_json, question_defination=question_definition_json, username=username)


#Test for test_db_data.html using new method
@app.route('/test_get_question_dict')
def test_get_question_dict():
    question_blank = get_question_dict("QUESTION_BLANK", 1)
    question_defination = get_question_dict("QUESTION_DEFINITION", 1)
    username = session.get('username')

    return render_template("test_get_dict.html", question_blank=question_blank, question_defination=question_defination, username=username)



############################################################################################################
# this is a prototype for the forget password page                                                         #
# in /forgetq, the user will be asked to enter the username                                                #
# in /forgetp, the user will be asked to enter the answers to the secure questions                         #
# if correct, user will be directed to /resetq, here the user will be asked to enter the new password      #
# if the password is entered, the user will be directed to /auth/resetq, where the password will be updated#
# after implementing, we have to delete the prototype content here                                         #
# and delete related resetq.html and forgetq.html files                                                    #
# current problems:                                                                                        #
# 1. if no user exists, no notice about wrong usernames                                                    #
# 2. if the answers are wrong, no notice about wrong answers                                               #
# 3. no way to check whether the password is secure                                                        #
# 4. no way to check whether the password is the same as the previous one                                  #
@app.route("/forgetq", methods=['GET'])
def forgetq():
    return render_template("forgetq.html")
# get the secure questions for the user, and send it to the resetq page
@app.route("/forgetp", methods=['POST'])
def forgetp():
    username = request.form.get('username')
    print(username)
    questions = show_secure_question(username)
    if not questions:
        return redirect(url_for('forgetq'))
    # return questions
    else:
        return render_template("resetq.html",username=username,questions=questions)
# to the reset password page, receive answers here and send it to the resetp route
@app.route("/resetq", methods=['GET'])
def resetq():
    username = request.form.get('username')
    return render_template("resetq.html",username=username)

@app.route("/auth/resetq", methods=['POST'])
def resetp():
    username = request.form.get('username')
    questions = show_secure_question(username)
    answer1 = request.form.get('answer1')
    answer2 = request.form.get('answer2')
    answers = [answer1,answer2]
    print(answers)
    # print(list_of_secure_questions)
    if check_secure_question(username, questions, answers):
        change_password = request.form.get('password')
        update("account", "password", change_password, f"username='{username}'")
        return redirect(url_for("home"))
    else:
        return redirect(url_for('forgetq'))

############################################################################################################
if __name__ == "__main__":
    app.run(debug=True, port=8888) # 端口8888