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

    #import key functions
from selenium.webdriver.common.keys import Keys


    #import time functionality
from time import sleep
from datetime import datetime

class nopCommerce_Productsearch:

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

    def currency_selection(self):
    # Select currency dropdown
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, Locator.Currency_selection_locator))).click()
    
    # Get the selected currency text
        US_dollar = self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.Currenct_selctor_US))).text
        EURO = self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.Currenct_selctor_EURO))).text
        
        # Get price text for comparison
        US_price = self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.US_price_locator))).text
        Euro_price = self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.Euro_price_locator))).text

        # Check conditions
        if "US Dollar" in US_dollar and US_price == '$1200':
            return True
        elif "Euro" in EURO and Euro_price == '€1032.00':
            return True
        else:
            return False
        
    
    def valid_search(self):
        
        # Wait for the search bar to be clickable and type the product name
        search_bar = self.wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        search_bar.click()
        search_bar.send_keys("HTC One Mini Blue")
        search_bar.send_keys(Keys.ENTER)

        # Wait for search results to load and assigning it to variable
        product_name = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'HTC One Mini Blue')]"))).text

        return product_name
    
    def invalid_search(self):
        
        # Wait for the search bar to be clickable and type the product name
        search_bar = self.wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        search_bar.click()
        search_bar.send_keys("12457")
        search_bar.send_keys(Keys.ENTER)

        # Wait for search results to load and assigning it to variable
        No_result = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "no-result"))).text

        return No_result
    
    def blank_search(self):
        
        # Wait for the search bar to be clickable and type the product name
        search_bar = self.wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        search_bar.click()
        search_bar.send_keys("")
        search_bar.send_keys(Keys.ENTER)

        # Wait for search results to load and assigning it to variable
        No_result = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "no-result"))).text

        return No_result

    def sorting_ZA(self):
    # Select any category (for example, "Electronics")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.Category_locator))).click()

    # Sort the products Z-A (select Z-A in the sorting dropdown)
        sort_dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "products-orderby")))
        sort_dropdown.click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[contains(text(),'Name: Z to A')]"))).click()

    # Verify the products are sorted from Z to A
    # Gets the product names after sorting and verify the order
        product_names = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='product-title']//a")))

    # Verify if the list is sorted in reverse alphabetical order (Z-A)
        sorted_correctly = True
        for i in range(1, len(product_names)):
            if product_names[i].text > product_names[i-1].text:
                sorted_correctly = False
                break

    def shutdown(self):
        self.driver.quit()
        return None



        
        