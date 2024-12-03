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

class nOpCommerce_AddtoCart:
    driver = webdriver.Chrome()
    ignored_exceptions = [NoSuchElementException, ElementNotVisibleException, ElementClickInterceptedException, TimeoutException]
    wait = WebDriverWait(driver, 50, poll_frequency=5, ignored_exceptions=ignored_exceptions)

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def start(self):
        self.driver.maximize_window()
        self.driver.get(Data.url)
        sleep(10)
        return True

    def add_to_cart(self):
        # Add product to cart
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button-2 product-box-add-to-cart-button']"))).click()
        message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content"))).text
        return message

    def edit_quantity_in_cart(self, product_name, new_quantity):
        # Navigate to cart
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Shopping cart')]"))).click()

        # Find the product row based on product name
        product_row = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{product_name}']/ancestor::tr")))
        
        # Update the quantity
        quantity_field = product_row.find_element(By.CLASS_NAME, "qty-input")
        quantity_field.clear()
        quantity_field.send_keys(new_quantity)

        # Update cart
        self.wait.until(EC.element_to_be_clickable((By.NAME, "updatecart"))).click()

        # Return the updated quantity value for assertion
        updated_quantity = product_row.find_element(By.CLASS_NAME, "qty-input").get_attribute("value")
        return int(updated_quantity)

    def verify_cart_total(self):
        # Navigate to cart
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Shopping cart')]"))).click()
        
        # Get the total price
        total_price = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-subtotal"))).text
        return total_price

    def remove_from_cart(self, product_name):
        # Navigate to cart
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Shopping cart')]"))).click()

        # Find the product row based on product name
        product_row = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{product_name}']/ancestor::tr")))
        
        # Remove the product
        product_row.find_element(By.NAME, "removefromcart").click()
        self.wait.until(EC.element_to_be_clickable((By.NAME, "updatecart"))).click()

        # Verify the cart is empty
        empty_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "no-data"))).text
        return empty_message
    
    def shutdown(self):
        self.driver.quit()
        return None

