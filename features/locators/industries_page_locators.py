"""
Industries Page Locators
Contains all locators specific to the Industries Page
"""

from selenium.webdriver.common.by import By


class IndustriesPageLocators:
    """Locators for Industries Page elements"""
    
    # Industry Sections (Currently in use)
    SECTION_TITLES = (By.CSS_SELECTOR, "div[data-type='text'] h3")
    LEARN_MORE_BUTTONS = (By.CSS_SELECTOR, "div[data-type='text'] div.btn-wrap a")
    
    # Dynamic Locators (Currently in use)
    @staticmethod
    def section_by_name(section_name):
        """Dynamic locator for section by name"""
        return (By.XPATH, f"(//h3[contains(text(), '{section_name}')])")
