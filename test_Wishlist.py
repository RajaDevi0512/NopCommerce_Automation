from ObjectModel.Wishlist import nOpCommerce_Wishlist

def test_start():
    assert nOpCommerce_Wishlist().start() == True
    print("Test Passed! Automation Started !")

def test_add_to_wishlist():
    assert nOpCommerce_Wishlist().add_to_wishlist() == "The product has been added to your wishlist"

def test_edit_wishlist_quantity():
    assert nOpCommerce_Wishlist.edit_wishlist_quantity() == "The wishlist has been updated successfully"

def test_verify_quantity_sum():
    assert nOpCommerce_Wishlist.verify_quantity_sum() == 2  # Assuming 2 is the desired quantity

def test_remove_from_wishlist():
    assert nOpCommerce_Wishlist.remove_from_wishlist() == "The wishlist is empty!"

def test_shutdown():
    assert nOpCommerce_Wishlist().shutdown() == None
    print("Test Passed! Automation shutdown!")
