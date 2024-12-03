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

class nopCommerce_Homepage:

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

    def homepage_check(self):
        # Wait for the homepage logo to be clickable and click on it
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.Home_page_logo))).click()
        
        # Wait for the banner to be loaded and present, and then assign it to 'banner'
        banner = self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.banner_icon)))
        
        # Return the 'banner' element
        return banner

    def facebook_handle(self):
        # Wait for the Facebook icon to be clickable and click on it
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.facebok_locator))).click()
        
        # Switch to the new tab that opened after clicking the Facebook icon
        self.driver.switch_to(self.driver.window_handles[-1])
        
        # Get the current URL of the Facebook page
        facebook_url = self.driver.current_url
        
        # Close the Facebook tab
        self.driver.close()
        
        # Switch back to the main window
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        # Return the Facebook URL
        return facebook_url


    def x_handle(self):
        # Wait for the X icon to be clickable and click on it
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.X_locator))).click()
        
        # Switch to the new tab that opened after clicking the X icon
        self.driver.switch_to(self.driver.window_handles[-1])
        
        # Get the current URL of the X page
        x_url = self.driver.current_url
        
        # Close the X tab
        self.driver.close()
        
        # Switch back to the main window
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        # Return the X URL
        return x_url


    def youtube_handle(self):
        # Wait for the YouTube icon to be clickable and click on it
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.youtube_locator))).click()
        
        # Switch to the new tab that opened after clicking the YouTube icon
        self.driver.switch_to(self.driver.window_handles[-1])
        
        # Get the current URL of the YouTube page (Note: there is a typo in the original code with `current_url0` which should be `current_url`)
        youtube_url = self.driver.current_url
        
        # Close the YouTube tab
        self.driver.close()
        
        # Switch back to the main window
        self.driver.switch_to.window(self.driver.window_handles[0])
        
        # Return the YouTube URL
        return youtube_url
    

    def category_check(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.Category_locator))).click()
        items = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, Locator.category_item_locator)))
        item_text=[]
        for item in items:
             if Data.desired_keywords.lower() in item_text.lower():
                keyword_found = True  # Mark as found
                break  # No need to check further keywords once one is found
        
        # If no keyword is found, fail the test and return False
        if not keyword_found:
            return False  # Return False if any item text does not contain a keyword
    
    # If all items contain at least one keyword, return True
        return True
    
    def shutdown(self):
        self.driver.quit()
        return None
