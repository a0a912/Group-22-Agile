# a simple login page using flask for testing the usermod.py
from flask import Flask, render_template, url_for, request, redirect, session
from user_crud_func import auth, sign_up, select_all
from usermod import execute, select_all, update
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

@app.route('/auth/forgot', methods=['GET'])
def forgot():
    return render_template("forgot.html")

@app.route('/auth/forgot', methods=['POST'])
def forgot_password():
    username = request.form.get('username')
    security_answer1 = request.form.get('security_answer1')
    security_answer2 = request.form.get('security_answer2')
    result = select_all("account", f"username='{username}'")
    if result:
        if result[0][3] == security_answer1 and result[0][4] == security_answer2:
            session['username'] = username
            return redirect(url_for('login_page'))
    return redirect(url_for('forgot'))

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
    username = session.get('username')
    return render_template("ranking.html", username=username)

@app.route('/profile', methods=['GET'])
def profile():
    username =session.get('username')
    return render_template("profile.html", username=username)

@app.route('/profile/update', methods=['POST'])
def update_password():
    username = session.get('username')
    password = request.form.get('password')
    # security_answer1 = request.form.get('security_answer1')
    # security_answer2 = request.form.get('security_answer2')
    update("account", "password", password, f"username='{username}'")
    return redirect(url_for('login_page')) 
   
    

if __name__ == "__main__":
    app.run(debug=True, port=8888) # 端口8888