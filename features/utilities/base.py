from selenium import webdriver
from data.data import data

def setup_driver():
    """
    Setup the Selenium WebDriver.
    :return: An instance of the Selenium WebDriver.
    """
    driver = webdriver.Chrome()
    driver.get(data["qa_url"])
    driver.maximize_window()
    driver.implicitly_wait(data["implicit_wait"]) 
    return driver

def get_page_title(driver):
    return driver.title

def get_current_url(driver):
    return driver.current_url

def close_driver(driver):
    driver.quit()
    print("Browser closed successfully.")