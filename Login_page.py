from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

from testData.data import Data
from testLocator.locator import Locator

    # import the webdriver wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    #import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from  selenium.common.exceptions import TimeoutException


    #import time functionality
from time import sleep
from datetime import datetime

class nopCommerce_Login:

    driver = webdriver.Chrome()
    ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException]
    wait = WebDriverWait(driver, 50, poll_frequency=5, ignored_exceptions=ignored_exceptions)

    def __init__(self):
         # Set up WebDriver
        self.driver = webdriver.Chrome()

        # Set up WebDriverWait
        self.wait = WebDriverWait(self.driver, 10)

      
    def start(self):
        self.driver.maximize_window()
        self.driver.get(Data.url)
        sleep(10)
        return True
    
    def correct_userName_password(self):
        # Wait for the login icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.login_icon))).click()
        
        # Wait for the email field and enter the valid username
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Email))).send_keys(Data.Valid_username)
        
        # Wait for the password field and enter the valid password
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.password))).send_keys(Data.Valid_password)
        
        # Wait for the "Remember Me" checkbox to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID,Locator.rememberMe_ID))).click()
        
        # Wait for the login button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.Login_button))).click()
        
        # Wait for the "My Account" element to be visible and get its text
        text = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,Locator.MyAccount_locator))).text
    
        # Pause for 30 seconds to ensure all actions are completed (optional)
        sleep(30)
        
        # Print the text to the console and return it
        print(text)
        return text

    def incorrect_userName_password(self):
      # Wait for the login icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.login_icon))).click()
        
        # Wait for the email field and enter the invalid username
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Email))).send_keys(Data.Invalid_username)
        
        # Wait for the password field and enter the invalid password
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.password))).send_keys(Data.Invalid_password)
        
        # Wait for the "Remember Me" checkbox to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID,Locator.rememberMe_ID))).click()
        
        # Wait for the login button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.Login_button))).click()
        
        # Wait for the error message for invalid email to be visible and get its text
        text2 = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,Locator.Email_ID_error))).text
        
        # Pause for 30 seconds to ensure all actions are completed (optional)
        sleep(30)
        
        # Print the error message to the console and return it
        print(text2)
        return text2

    def incorrect_userName_correctPassword(self):
        # Wait for the login icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.login_icon))).click()
        
        # Wait for the email field and enter the invalid username
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Email))).send_keys(Data.Invalid_username)
        
        # Wait for the password field and enter the valid password
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.password))).send_keys(Data.Valid_password)
        
        # Wait for the "Remember Me" checkbox to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID,Locator.rememberMe_ID))).click()
        
        # Wait for the login button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.Login_button))).click()
        
        # Wait for the error message for invalid password to be visible and get its text
        text3 = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,Locator.Password_error))).text
        
        # Pause for 30 seconds to ensure all actions are completed (optional)
        sleep(30)
        
        # Print the error message to the console and return it
        print(text3)
        return text3

    def correct_userName_incorrectPassword(self):
        # Wait for the login icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.login_icon))).click()
        
        # Wait for the email field and enter the valid username
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Email))).send_keys(Data.Valid_username)
        
        # Wait for the password field and enter the invalid password
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.password))).send_keys(Data.Invalid_password)
        
        # Wait for the "Remember Me" checkbox to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID,Locator.rememberMe_ID))).click()
        
        # Wait for the login button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.Login_button))).click()
        
        # Wait for the error message for invalid email to be visible and get its text
        text4 = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME,Locator.Email_ID_error))).text
        
        # Pause for 30 seconds to ensure all actions are completed (optional)
        sleep(30)
        
        # Print the error message to the console and return it
        print(text4)
        return text4

    
    def shutdown(self):
        self.driver.quit()
        return None
