from ObjectModel.registration_page import nopCOmmerce_Registration


def test_start():
    assert nopCOmmerce_Registration().start() == True
    print("Test Passed! Automation Started !")
# Asserting the valid registration with registration confirmation message
def test_validregister():
    assert nopCOmmerce_Registration().valid_registration() == "Your registration completed"
    print("Test Passed! Completed Registration!")

# Asserting the registration with blank details 
def test_blankregistration():
    assert nopCOmmerce_Registration().blank_registration() == "First name is required."
    print("Test Passed! Missing fields required")

# Asserting the registration with invalid details
def test_invalidregistration():
    assert nopCOmmerce_Registration().invalid_registration() == "Wrong email"
    print("Test Passed! Invalid Mail ID")

# Asserting the registration with invalid details with mail Id satisfy the li ul conditions
def test_invalidregistration2():
    assert nopCOmmerce_Registration().invalid_registration() == "Wrong email"
    print("Test Failed! Mail id registered")

def test_shutdown():
    assert nopCOmmerce_Registration().shutdown() == None
    print("Test Passed! Automation shutdown!")