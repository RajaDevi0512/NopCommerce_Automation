class Locator:
#Registration part
    registration_icon = 'ico-register' #CLass
    gender_male = 'gender-male' #ID
    firstName_locator  = 'FirstName #' #ID
    lastName_locator ='LastName' #ID
    Day = 'DateOfBirthDay' # Name 
    Select_day = "//select[@name='DateOfBirthDay']/option[14]" #Class
    Month = 'DateOfBirthMonth'#Name
    select_month = "//select[@name='DateOfBirthMonth']/option[11]" #Class
    Year = 'DateOfBirthYear' #Name
    select_year = "//select[@name='DateOfBirthYear']/option[100]" #class
    Registartion_password = "Password" #ID 
    Confirm_password = "ConfirmPassword" #ID
    register_button = 'register-button' #ID
    registration_message_confirmation = "//div[@class='page-body']/div"
    Missing_meessage = "FirstName-error" #ID
    Missing_Mail = "Email-error" #ID

#Login Locators
    login_icon = 'ico-login' #class
    Email = 'Email' #ID
    password = 'Password' #ID
    rememberMe_ID = 'RememberMe' #ID
    Login_button = "//button[contains(text(), 'Log in')]"
    MyAccount_locator = 'ico-account' #class
    Confirm_password = 'ConfirmPassword' #ID
    Email_ID_error = "Email-error" #ID
    Password_error = "//div[@class='message-error validation-summary-errors']/ul/li" #Xpath

#HomePage Locators
    Home_page_logo = "header-logo" #Class
    banner_icon= "//div[@id='nivo-slider']/a" #XPATH
    facebok_locator = "//li[@class='facebook']/a" #XPATH
    X_locator ="//li[@class='twitter']/a " #XPATH
    youtube_locator = "//li[@class='youtube']/a" #XPATH
    Category_locator = "//a[contains(text(), 'Jewelry')][1]"#XPATH
    category_item_locator = "//h2[@class='product-title']/a" #XPATH

#Product Browsing & Pricing
    Currency_selection_locator = 'customerCurrency' #ID
    Currenct_selctor_US = "//select[@id ='customerCurrency']/option[1]" #XPATH
    Currenct_selctor_EURO= "//select[@id ='customerCurrency']/option[2]" #XPATH
    US_price_locator = "//span[contains(text(),'$1,200.00')]" #XPATH
    Euro_price_locator = "//span[contains(text(),'€1032.00')]" #XPATH