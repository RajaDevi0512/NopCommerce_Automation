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

  #import time functionality
from time import sleep
from datetime import datetime

    #import exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from  selenium.common.exceptions import TimeoutException

class nopCOmmerce_Registration:
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
     
     def valid_registration(self):
        # Wait for the registration icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.registration_icon))).click()
        
        # Wait for the gender selection and click male
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.gender_male))).click()
        
        # Wait for the first name field and enter the first name
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.firstName_locator))).send_keys(Data.FirstName)
        
        # Wait for the last name field and enter the last name
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.lastName_locator))).send_keys(Data.LastName)
        
        # Select the day from the dropdown
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Day))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.Select_Day))).click()
        
        # Select the month from the dropdown
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Month))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.select_month))).click()
        
        # Select the year from the dropdown
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Year))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.select_year))).click()
        
        # Wait for the email field and enter the valid email
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.Email))).send_keys(Data.Valid_username)
        
        # Wait for the registration password field and enter the valid password
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Registartion_password))).send_keys(Data.Valid_password)
        
        # Wait for the confirm password field and confirm the valid password
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Confirm_password))).send_keys(Data.Valid_password)
        
        # Wait for the register button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID, Locator.register_button))).click()
        
        # Wait for the registration confirmation message and get the text
        registration_message = self.wait.until(EC.presence_of_element_located((By.XPATH,Locator.registration_message_confirmation))).text
        return registration_message

     def blank_registration(self):
        # Wait for the registration icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.registration_icon))).click()
        
        # Wait for the gender selection and click male
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.gender_male))).click()
        
        # Enter blank first name and last name
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.firstName_locator))).send_keys(Data.blank_Name)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.lastName_locator))).send_keys(Data.blank_Name)
        
        # Enter blank email
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.Email))).send_keys(Data.blank_Mail)
        
        # Enter blank password and confirm password
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Registartion_password))).send_keys(Data.blan_password_atregister)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Confirm_password))).send_keys(Data.blan_password_atregister)
        
        # Wait for the register button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID, Locator.register_button))).click()
        
        # Wait for the registration fail message and get the text
        registration_Failmessage = self.wait.until(EC.presence_of_element_located((By.XPATH,Locator.Missing_meessage))).text
        return registration_Failmessage

     def invalid_registration(self):
        # Wait for the registration icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.registration_icon))).click()
        
        # Wait for the gender selection and click male
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.gender_male))).click()
        
        # Enter invalid first name and last name
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.firstName_locator))).send_keys(Data.invalid_Name)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.lastName_locator))).send_keys(Data.invalid_Name)
        
        # Select the day, month, and year from the dropdown
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Day))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.Select_Day))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Month))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.select_month))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Year))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.select_year))).click()
        
        # Enter invalid email and password
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.Email))).send_keys(Data.invalid_mailID)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Registartion_password))).send_keys(Data.Invalid_password)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Confirm_password))).send_keys(Data.Invalid_password)
        
        # Wait for the register button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID, Locator.register_button))).click()
        
        # Wait for the registration fail message for invalid email and get the text
        registration_Failmessage1 = self.wait.until(EC.presence_of_element_located((By.XPATH,Locator.Missing_Mail))).text
        return registration_Failmessage1

     def invalid_registration2(self):
        # Wait for the registration icon to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.registration_icon))).click()
        
        # Wait for the gender selection and click male
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.gender_male))).click()
        
        # Enter invalid first name and last name
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.firstName_locator))).send_keys(Data.invalid_Name)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.lastName_locator))).send_keys(Data.invalid_Name)
        
        # Select the day, month, and year from the dropdown
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Day))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.Select_Day))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Month))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.select_month))).click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, Locator.Year))).click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.select_year))).click()
        
        # Enter invalid username and password
        self.wait.until(EC.presence_of_element_located((By.ID,Locator.Email))).send_keys(Data.Invalid_username)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Registartion_password))).send_keys(Data.Invalid_password)
        self.wait.until(EC.presence_of_element_located((By.ID, Locator.Confirm_password))).send_keys(Data.Invalid_password)
        
        # Wait for the register button to be clickable and click it
        self.wait.until(EC.element_to_be_clickable((By.ID, Locator.register_button))).click()
        
        # Wait for the registration fail message for invalid email and get the text
        registration_Failmessage1 = self.wait.until(EC.presence_of_element_located((By.XPATH,Locator.Missing_Mail))).text
        return registration_Failmessage1

        
     def shutdown(self):
            self.driver.quit()
            return None