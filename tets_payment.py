from ObjectModel.payment import nOpCommerce_Payment

def test_start():
    assert nOpCommerce_Payment().start() == True
    print("Test Passed! Automation Started !")

def test_payment_info_submission(setup):
    driver, wait = setup
    payment = nOpCommerce_Payment(driver, wait)
    
    # Test entering valid payment information
    success_message = payment.enter_payment_info()
    assert "Your order has been successfully processed!" in success_message
    print("Payment info submission test passed!")

def test_shutdown():
    assert nOpCommerce_Payment().shutdown() == None
    print("Test Passed! Automation shutdown!")
