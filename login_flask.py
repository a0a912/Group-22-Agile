# a simple login page using flask for testing the usermod.py
from flask import Flask, render_template, url_for, request, redirect
from user_crud_func import auth, sign_up, select_id
app = Flask(__name__)
# page of login when you open the website 127.0.0.1:8888/
@app.route('/')
def home():
    return render_template("login.html")

@app.route('/register')
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
        # if the user is authenticated then redirect to the home page with the username
        return render_template('home.html', username=username)
    # if the user is not authenticated then redirect to the login page
    return redirect(url_for('home'))

# register route making a post request to the server to check the username and password using the sign_up function from usermod.py
@app.route('/auth/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    result = sign_up(username, password)
    if result[0]:
        return redirect(url_for('home'))
    return redirect(url_for('register_page'))

# @app.route('/question', methods=['GET'])
# def question():
#     """
#     return render_template("question.html", question=question,word=word, incorrect=incorrect_list)
#     # in html
#     <h1 id = 'question_text'>{{ question }}</h1>
#     {{% for choice in choices %}}
#     <form id = 'question_form'>
    
#     """
#     return render_template("question.html",question=question)

#make the get to put information in question page
@app.route('/question', methods=['GET'])
def get_question():
    question = select_id('QUESTION_BLANK', 1, 'example')[0]
    correct = select_id('QUESTION_BLANK', 1, 'correct')[0]
    return redirect(url_for('load_question', question=question, correct=correct))
    # return redirect(url_for('question'), question=question,correct,incorrect)

@app.route('/question/load', methods=['POST', 'GET'])
def load_question():
    question = request.args.get('question')
    correct = request.args.get('correct')
    return render_template("question.html", question=question, correct=correct)

    # return redirect(url_for('question'), question=question,correct,incorrect)

if __name__ == "__main__":
    app.run(debug=True, port=8888) # 端口8888