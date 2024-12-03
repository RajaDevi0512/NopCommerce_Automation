from ObjectModel.Homepage import nopCommerce_Homepage

def test_start():
    assert nopCommerce_Homepage().start() == True
    print("Test Passed! Automation Started !")

# Asserting nopcommerce logo returns to homepage containing slide show/banner
def test_homepagelogo():
    assert nopCommerce_Homepage().homepage_check().is_displayed
    print("Test Passed!")

# Asserting facebook handle leads to faceboom page
def test_facebookhandle():
    assert nopCommerce_Homepage().facebook_handle() == "https://www.facebook.com/nopCommerce"
    print("Test Passwd")

# Asserting x handle leads to X page
def test_xhandle():
    assert nopCommerce_Homepage().x_handle() == "https://x.com/nopCommerce"
    print("Test Passwd")

# Asserting youtube handle leads to youtube page
def test_youtubehandle():
    assert nopCommerce_Homepage().youtube_handle() == "https://www.youtube.com/user/nopCommerce"
    print("Test Passwd")

# Category should contains mentioned products such as jewlry should have ring, bracelet and necklace
def test_categoryCheck():
    assert nopCommerce_Homepage().category_check() == True
    print("Test Passed")

def test_shutdown():
    assert nopCommerce_Homepage().shutdown() == None
    print("Test Passed! Automation shutdown!")