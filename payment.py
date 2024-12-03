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

class nOpCommerce_Payment:
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

    def enter_payment_info(self):
        # Navigate to the payment page
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Checkout')]"))).click()

        # Fill in the billing information
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("John")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))).send_keys("Doe")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))).send_keys("john.doe@example.com")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))).send_keys("United States")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))).send_keys("New York")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))).send_keys("123 Elm St")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))).send_keys("10001")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))).send_keys("1234567890")

        # Select shipping method
        self.wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1"))).click()

        # Fill in the payment method (Credit Card)
        self.wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))).send_keys("MasterCard")
        self.wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("John Doe")
        self.wait.until(EC.presence_of_element_located((By.ID, "CardNumber"))).send_keys("4111111111111111")
        self.wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth"))).send_keys("12")
        self.wait.until(EC.presence_of_element_located((By.ID, "ExpireYear"))).send_keys("2026")
        self.wait.until(EC.presence_of_element_located((By.ID, "CardCode"))).send_keys("123")

        # Click continue to submit the payment information
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 payment-method-next-step-button']"))).click()

        # Verify payment is successful (confirm confirmation message)
        success_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "order-completed"))).text
        return success_message
    
    def shutdown(self):
        self.driver.quit()
        return None

