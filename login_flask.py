# a simple login page using flask for testing the usermod.py
from flask import Flask, render_template, url_for, request, redirect
from usermod import auth
app = Flask(__name__)
# page of login when you open the website 127.0.0.1:8888/
@app.route('/')
def home():
    return render_template("login.html")
# login route making a post request to the server to check the username and password using the auth function from usermod.py
@app.route('/auth/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    if auth(username, password):
        # if the user is authenticated then redirect to the home page with the username
        return render_template('home.html', username=username)
    # if the user is not authenticated then redirect to the login page
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=8888) # 端口8888