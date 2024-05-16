from user_crud_func import sign_up

def test_sign_up():
    # Test case for successful sign up
    result, message = sign_up("test!", "Password1!", "What is your favorite color?", "Blue", "What is your favorite food?", "Pizza")
    assert result == True, "Expected True, but got False"
    assert message == "User created", f"Expected 'User created', but got {message}"

    # Test case for existing user 
    result, message = sign_up("test!", "Password1!", "What is your favorite color?", "Blue", "What is your favorite food?", "Pizza")
    assert result == False, "Expected False, but got True"
    assert message == "User already exists", f"Expected 'User already exists', but got {message}"

    # Test case for short username (3 letters)
    result, message = sign_up("tes", "Password1!", "What is your favorite color?", "Blue", "What is your favorite food?", "Pizza")
    assert result == False, "Expected False, but got True"
    assert message == "Username should be at least 4 characters", f"Expected 'Username should be at least 4 characters', but got {message}"

    # Test case for short password (5 letters)
    result, message = sign_up("test2", "Pass1", "What is your favorite color?", "Blue", "What is your favorite food?", "Pizza")
    assert result == False, "Expected False, but got True"
    assert message == "Password should be at least 6 characters", f"Expected 'Password should be at least 6 characters', but got {message}"

    # Test case for password without uppercase, lowercase, digit and special character
    result, message = sign_up("test3", "password", "What is your favorite color?", "Blue", "What is your favorite food?", "Pizza")
    assert result == False, "Expected False, but got True"
    assert message == "Password should contain at least one uppercase letter, one lowercase letter, one digit and one special character", f"Expected 'Password should contain at least one uppercase letter, one lowercase letter, one digit and one special character', but got {message}"

    # Test case for missing any secure question answers
    result, message = sign_up("test4", "Password1!", "What is your favorite color?", "Blue", "What is your favorite food?", "")
    assert result == False, "Expected False, but got True"
    assert message == "Please answer all the security questions", f"Expected 'Please answer all the security questions', but got {message}"
    
if __name__ == "__main__":
    test_sign_up()
    print("All tests passed")