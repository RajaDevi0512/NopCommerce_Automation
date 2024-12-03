from ObjectModel.ProductSearch_pricing import nopCommerce_Productsearch

def test_start():
    assert nopCommerce_Productsearch().start() == True
    print("Test Passed! Automation Started !")

# Us should show US dollar while Euro should show Euro
def test_currency_selector():
    assert nopCommerce_Productsearch().currecny_selection() == True
    print("Test Passed")

# Assert that the product with the exact name is present in the search results
def test_validsearch():
    assert nopCommerce_Productsearch().valid_search() == "HTC One Mini Blue"
    print("Test Passed!!")

# Assert that the product with invalid name to get "No result found"
def test_invalidSearch():
    assert nopCommerce_Productsearch().invalid_search() == "No products were found that matched your criteria."
    print("Test Passed")

# Assert that the product in Z-A order
def test_invalidSearch():
    assert nopCommerce_Productsearch().sorting_ZA() == True
    print("Test Passed")

def test_shutdown():
    assert nopCommerce_Productsearch().shutdown() == None
    print("Test Passed! Automation shutdown!")
