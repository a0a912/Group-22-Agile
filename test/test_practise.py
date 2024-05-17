import sys
import os
import pytest
from flask import Flask, session, url_for

# Ensure the correct directories are in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from login_flask import app
import manage
from user_crud_func import auth, sign_up, select_all, show_secure_question, update

@pytest.fixture
def client():
    """
    This is a pytest fixture that sets up a Flask test client.
    It's used to test our Flask application.

    This fixture does the following:
        1. Sets the 'TESTING' configuration variable to True. This is necessary
           for Flask to know that we are running tests.
        2. Creates a test client. The test client is used to send HTTP requests
           to our application and check the responses.
        3. Sets up the application context. This is necessary for Flask to know
           that we are running tests and should use the test configuration.
        4. Yields the test client. The test client is then passed to the test
           function.
        5. Cleans up the test client.

    This fixture is used in the test functions.
    """

    # Set the 'TESTING' configuration variable to True.
    app.config['TESTING'] = True

    # Create a test client.
    with app.test_client() as client:

        # Set up the application context.
        with app.app_context():

            yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200

def test_user_logged_in(client):
    """
    This test checks if the user is logged in by setting a username in the session
    and then verifying that the username is accessible on the homepage.
    """
    with client.session_transaction() as session:
        session['username'] = 'testuser'

    response = client.get('/')
    assert response.status_code == 200
    assert b'testuser' in response.data


def test_logout_redirect(client):
    """
    This test checks if logging out correctly redirects to the homepage.

    The test performs the following steps:
        1. Logs in the user by setting the session using the 'username' key.
        2. Performs a POST request to the '/logout' endpoint, simulating a logout action.
        3. Checks that the response status code is 302, which is the status code for redirection.
        4. Checks that the redirection target is '/', which is the homepage.
    """

    # Log in the user by setting the session
    # This is simulating a successful login by setting the 'username' key in the session.
    # This is equivalent to setting the user's authentication status to true.
    with client.session_transaction() as session:
        session['username'] = 'testuser'

    # Perform the logout action
    # This sends a POST request to the '/logout' endpoint, which is expected to handle the logout logic.
    response = client.post('/logout')

    # Check that the response status code is 302, indicating a redirection.
    # This confirms that the logout action redirected the user to the homepage.
    assert response.status_code == 302

    # Check the redirection target
    # This confirms that the redirection target is '/', which is the homepage.
    # This confirms that the user is redirected to the homepage after logging out.
    assert response.headers['Location'] == '/'
