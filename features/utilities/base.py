from selenium import webdriver
from data.data import data
from utilities.read_properties import ReadConfig

def setup_driver():
    """
    Setup the Selenium WebDriver.
    :return: An instance of the Selenium WebDriver.
    """
    driver = webdriver.Chrome()
    #driver.get(data["qa_url"])
    driver.get(ReadConfig.get_app_url())
    driver.maximize_window()
    #driver.implicitly_wait(data["implicit_wait"]) 
    return driver

def search_index_by_title(titles, title):
    """
    Search for the index of a title in a list of titles.
    :param titles: List of title elements.
    :param title: The title to search for.
    :return: The index of the title if found, otherwise -1.
    """
    for i in range(len(titles)):
        if titles[i].text == title:
            return i
    return -1  # Return -1 if not found (moved outside the loop)


def close_driver(driver):
    driver.quit()
    