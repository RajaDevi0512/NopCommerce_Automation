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

class nOpCommerce_Wishlist:

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
    
    # Add product to wishlist
    def add_to_wishlist(self):
        product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'HTC One Mini Blue')]")))
        product.click()
        add_to_wishlist_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "add-to-wishlist-button-19")))
        add_to_wishlist_btn.click()
        wishlist_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content"))).text
        return wishlist_message

    # Edit quantities in wishlist
    def edit_wishlist_quantity(self):
        quantity_input = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "qty-input")))
        quantity_input.clear()
        quantity_input.send_keys("2")
        update_btn = self.wait.until(EC.element_to_be_clickable((By.NAME, "updatecart")))
        update_btn.click()
        updated_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content"))).text
        return updated_message

    # Verify sum of product quantities in wishlist
    def verify_quantity_sum(self):
        quantities = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "qty-input")))
        total_quantity = sum(int(quantity.get_attribute("value")) for quantity in quantities)
        return total_quantity

    # Remove product from wishlist
    def remove_from_wishlist(self):
        remove_btn = self.wait.until(EC.element_to_be_clickable((By.NAME, "removefromcart")))
        remove_btn.click()
        empty_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "no-data"))).text
        return empty_message
    
    def shutdown(self):
        self.driver.quit()
        return None

