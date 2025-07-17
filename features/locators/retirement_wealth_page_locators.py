"""
Retirement Wealth Page Locators
Contains all locators specific to the Retirement Wealth Page
"""

from selenium.webdriver.common.by import By


class RetirementWealthPageLocators:
    """Locators for Retirement Wealth Page elements"""
    
    # Cards Section (Currently in use)
    CARD_FRONT_TEXT = (By.CSS_SELECTOR, "div.card-front-inner div.card-text")
    CARD_WRAPPER = (By.CSS_SELECTOR, "div.card-wrapper")
    CARD_SMALL_TEXT = (By.CSS_SELECTOR, "div.card-text.small")
    
    # Action Buttons (Currently in use)
    GET_STARTED_BUTTON = (By.LINK_TEXT, "Let's get started")
    
    # Dynamic Locators (Currently in use)
    @staticmethod
    def card_by_text(text):
        """Dynamic locator for card by text content"""
        return (By.XPATH, f"(//div[contains(text(), '{text}')])")