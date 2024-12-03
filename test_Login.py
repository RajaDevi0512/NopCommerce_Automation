"""
test_login file contains all the test cases
"""
from ObjectModel.Login_page import nopCommerce_Login


def test_start():
    assert nopCommerce_Login().start() == True
    print("Test Passed! Automation Started !")

# Asserting the valid login with Myaccount text
def test_validusername_password():
    assert nopCommerce_Login().correct_userName_password() == "My account"
    print("Test Pass ! Valid Login !")

# Asserting the wrong username and wrong password with "Wrong mail"
def test_invalid_username_validPassword():
    assert nopCommerce_Login().incorrect_userName_password() == "Wrong email"
    print("Test Passed! Invalid mail ID !")

# Asserting the valid username with wrong password with "Wrong Creditials"
def test_ValidUsername_invalidPassword():
    assert nopCommerce_Login().incorrect_userName_correctPassword() == "The credentials provided are incorrect"
    print("Test Passed! Wrong Credentials !")

# Asserting the Invalid username and valid password with "Wrong Credentials"
def test_InvalidUsername_ValidPassword():
    assert nopCommerce_Login().incorrect_userName_correctPassword() == "The credentials provided are incorrect"
    print("Test Passed! Wrong Email !")

def test_shutdown():
    assert nopCommerce_Login().shutdown() == None
    print("Test Passed! Automation shutdown!")
