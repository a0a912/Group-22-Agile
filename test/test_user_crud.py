import unittest
from user_crud_func import sign_up, check_password

class TestUserCrudFunc(unittest.TestCase):

    def test_sign_up_short_username(self):
        result = sign_up("usr", "password1", "question1", "answer1", "question2", "answer2")
        self.assertEqual(result, (False, "Username should be at least 4 characters"))

    def test_sign_up_short_password(self):
        result = sign_up("username", "pass1", "question1", "answer1", "question2", "answer2")
        self.assertEqual(result, (False, "Password should be at least 6 characters"))

    def test_sign_up_invalid_password(self):
        result = sign_up("username", "password", "question1", "answer1", "question2", "answer2")
        self.assertEqual(result, (False, "Password should contain at least one uppercase letter, one lowercase letter, one digit and one special character"))

    def test_check_password_short(self):
        self.assertFalse(check_password("Pass1"))

    def test_check_password_no_digit(self):
        self.assertFalse(check_password("Password!"))

    def test_check_password_no_uppercase(self):
        self.assertFalse(check_password("password1!"))

    def test_check_password_no_lowercase(self):
        self.assertFalse(check_password("PASSWORD1!"))

    def test_check_password_no_special(self):
        self.assertFalse(check_password("Password1"))

    def test_check_password_valid(self):
        self.assertTrue(check_password("Password1!"))

if __name__ == "__main__":
    unittest.main()