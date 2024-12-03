from ObjectModel.add_to_Cart import nOpCommerce_AddtoCart

def test_start():
    assert nOpCommerce_AddtoCart().start() == True
    print("Test Passed! Automation Started !")

def test_add_to_cart(setup):
    driver, wait = setup
    cart = nOpCommerce_AddtoCart(driver, wait)
    
    # Test adding product to cart
    message = cart.add_to_cart()
    assert "The product has been added to your shopping cart" in message
    print("Add to cart test passed!")

def test_edit_quantity_in_cart(setup):
    driver, wait = setup
    cart = nOpCommerce_AddtoCart(driver, wait)
    
    # Test editing quantity
    updated_quantity = cart.edit_quantity_in_cart("HTC One Mini Blue", 3)
    assert updated_quantity == 3
    print("Edit quantity test passed!")

def test_verify_cart_total(setup):
    driver, wait = setup
    cart = nOpCommerce_AddtoCart(driver, wait)
    
    # Test verifying cart total
    total_price = cart.verify_cart_total()
    assert total_price != ""
    print("Verify cart total test passed!")

def test_remove_from_cart(setup):
    driver, wait = setup
    cart = nOpCommerce_AddtoCart(driver, wait)
    
    # Test removing product from cart
    empty_message = cart.remove_from_cart("HTC One Mini Blue")
    assert "Your Shopping Cart is empty!" in empty_message
    print("Remove from cart test passed!")


def test_shutdown():
    assert nOpCommerce_AddtoCart().shutdown() == None
    print("Test Passed! Automation shutdown!")