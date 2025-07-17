from seleniumpagefactory import PageFactory
from selenium.common.exceptions import NoSuchElementException
from locators.home_page_locators import HomePageLocators

class HomePage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
    
    # Using centralized locators from HomePageLocators
    locators = {
        "accept_cookies_button": HomePageLocators.ACCEPT_COOKIES_BUTTON,
    }

    def accept_cookies(self):
        """
        Accept cookies by clicking the accept button.
        raise an exception if the button is not found or already accepted.
        """
        try:
            self.accept_cookies_button.click()
        except NoSuchElementException:
            print("No cookies button found or already accepted.")
    
    def click_on_header_navigation_link(self, link_text):
        """
        Click on a header navigation link by its text.
        param link_text: The text of the link to click.
        """
        # Using dynamic locator from centralized HomePageLocators
        self.driver.find_element(*HomePageLocators.navigation_link_by_text(link_text)).click()