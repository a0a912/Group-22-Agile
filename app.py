
from model import Word
#get sqite3
import sqlite3
# a simple login page using flask for testing the usermod.py
from flask import Flask, render_template, url_for, request, redirect
from user_crud_func import auth, sign_up
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

#Test to see if I can throw db data onto the website
@app.route('/test')
def test():
    #Read database.db and get all the entries in the QUESTION_BLANK table
    connection = sqlite3.connect('./database/database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM QUESTION_BLANK")
    data = cursor.fetchall()
    
    return render_template('test_db_data.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, port=8888) # 端口8888