import pytest
from login_flask import app as flask_app  

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_forgot_password(client):
    # Answers the secure questions with correct answers
    data = {
        "username": "testuser",
        "secure_question1": "What is your favorite color?",
        "answer1": "Blue",
        "secure_question2": "What is your favorite food?",
        "answer2": "Pizza",
        "new_password": "New123!"
    }

    # Make a POST request to the forgot route and redirect to the forgot route
    response = client.post("/auth/forgot", data=data)

    # Check that the user is redirected to the forgot route
    assert response.status_code == 302  
    with client.session_transaction() as session:
        assert 'username' in session
        assert 'questions' in session

    # Make a POST request to the answer route
    response = client.post("/auth/forgot/answer", data=data)

    # Check that the password was updated and user is redirected to the home route
    assert response.status_code == 302  # Redirect status code

def test_forgot_password_wrong_answers(client):
    # Answers the secure questions with wrong answers
    data = {
        "username": "testuser",
        "secure_question1": "What is your favorite color?",
        "answer1": "Green",  # Wrong answer
        "secure_question2": "What is your favorite food?",
        "answer2": "Kimchi",  # Wrong answer
        "new_password": "New123!"
    }

    # Make a POST request to the forgot route
    response = client.post("/auth/forgot", data=data)

    # Check that the user is redirected to the forgot route again as the answers are wrong
    assert response.status_code == 302  # Redirect status code
    
