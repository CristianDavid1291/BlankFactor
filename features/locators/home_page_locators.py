"""
Home Page Locators
Contains all locators specific to the Home Page
"""

from selenium.webdriver.common.by import By


class HomePageLocators:
    """Locators for Home Page elements"""
    
    # Cookie Management (Currently in use)
    ACCEPT_COOKIES_BUTTON = (By.XPATH, "(//button[contains(text(), 'Accept All')])[1]")
    
    # Dynamic Locators (Currently in use)
    @staticmethod
    def navigation_link_by_text(link_text):
        """Dynamic locator for navigation links by text"""
        return (By.LINK_TEXT, link_text)
    
    @staticmethod
    def navigation_link_by_partial_text(partial_text):
        """Dynamic locator for navigation links by partial text"""
        return (By.PARTIAL_LINK_TEXT, partial_text)
    
    @staticmethod
    def section_by_id(section_id):
        """Dynamic locator for sections by ID"""
        return (By.ID, section_id)
    
    @staticmethod
    def button_by_text(button_text):
        """Dynamic locator for buttons by text"""
        return (By.XPATH, f"//button[contains(text(), '{button_text}')]")
    
    @staticmethod
    def heading_by_text(heading_text):
        """Dynamic locator for headings by text"""
        return (By.XPATH, f"//*[self::h1 or self::h2 or self::h3][contains(text(), '{heading_text}')]")
