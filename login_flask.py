# a simple login page using flask for testing the usermod.py
from flask import Flask, render_template, url_for, request, redirect, session
from model import Word, get_question_dict
from user_crud_func import auth, sign_up, select_all
import json
import secrets 

app = Flask(__name__)
app.secret_key = "d4413d05138d1fa03489e233df6aca24"

# page of login when you open the website 127.0.0.1:8888/
@app.route('/', methods=['GET'])
def home():
    username = session.get('username')
    return render_template("home.html", username=username)

@app.route('/login', methods=['GET'])
def login_page():
    return render_template("login.html")

@app.route('/register', methods=['GET'])
def register_page():
    return render_template("register.html")

# login route making a post request to the server to check the username and password using the auth function from usermod.py
@app.route('/auth/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    # print(username, password)
    result = auth(username, password)
    # print(result)
    if result[0]:
        session['username'] = username
        # if the user is authenticated then redirect to the home page with the username
        return redirect(url_for('home'))
    # if the user is not authenticated then redirect to the login page
    return redirect(url_for('home'))

# register route making a post request to the server to check the username and password using the sign_up function from usermod.py
@app.route('/auth/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    result = sign_up(username, password)
    if result[0]:
        return redirect(url_for('login_page'))
    return redirect(url_for('register_page'))

@app.route('/auth/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/quiz', methods=['GET'])
def quiz():
    username = session.get('username')
    return render_template("quiz.html", username=username)

@app.route('/quiz/submit', methods=['POST'])
def submit():
    return 

@app.route('/ranking', methods=['GET'])
def ranking():
    scores = select_all("account", "username, score")
    return render_template("scores.html", scores=scores)

@app.route('/profile', methods=['GET'])
def profile():
    username =session.get('username')
    return render_template("profile.html", username=username)


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


if __name__ == "__main__":
    app.run(debug=True, port=8888) # 端口8888