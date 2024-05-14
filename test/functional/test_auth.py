# from usermod import auth





# def test_auth():
#     assert auth("ahmed", "ahmed123") == True
#     assert auth("ahmed", "ahmed") == False
#     assert auth("admin", "admin") == True
#     assert auth("admin", "admin123") == False

def test_home():
    flask_app = login_flask()

    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b'English Learning Web Platform' in response.data
        assert b'Unolingo' in response.data

