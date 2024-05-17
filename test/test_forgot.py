import pytest
from flask import session
from login_flask import app as flask_app  

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_forgot_password(client):
    # User's data
    data = {
        "username": "testuser",
        "secure_question1": "What is your favorite color?",
        "answer1": "Blue",
        "secure_question2": "What is your favorite food?",
        "answer2": "Pizza",
        "new_password": "New!1"
    }

    # Make a POST request to the forgot route
    response = client.post("/auth/forgot", data=data)

    # Check that the user is redirected to the answer route
    assert response.status_code == 302  # Redirect status code
    with client.session_transaction() as sess:
        assert 'username' in sess
        assert 'questions' in sess

    # Make a POST request to the answer route
    response = client.post("/auth/forgot/answer", data=data)

    # Check that the password was updated and user is redirected to the home route
    assert response.status_code == 302  # Redirect status code

def test_forgot_password_wrong_answers(client):
    # User's data
    data = {
        "username": "testuser",
        "secure_question1": "What is your favorite color?",
        "answer1": "Green",  # Wrong answer
        "secure_question2": "What is your favorite food?",
        "answer2": "Burger",  # Wrong answer
        "new_password": "New!1"
    }

    # Make a POST request to the forgot route
    response = client.post("/auth/forgot", data=data)

    # Check that the user is redirected to the forgot route again as the answers are wrong
    assert response.status_code == 302  # Redirect status code
    
    