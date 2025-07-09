from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By

class HomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
    
    locators = {
        "accept_cookies_button": (By.XPATH,"(//button[contains(text(), 'Accept All')])[1]"),
    }

    def accept_cookies(self):
        """
        Accept cookies by clicking the accept button.
        raise an exception if the button is not found or already accepted.
        """
        try:
            self.accept_cookies_button.click()
        except Exception as e:
            print(f"No cookies button found or already accepted. {e}")
    
    def click_on_header_navigation_link(self, link_text):
        """
        Click on a header navigation link by its text.
        param link_text: The text of the link to click.
        """
        self.driver.find_element(By.LINK_TEXT, link_text).click()