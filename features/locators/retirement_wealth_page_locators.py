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
    NEXT_SECTION_BUTTON = (By.CSS_SELECTOR, ".next-section-btn")
    SCROLL_TO_TOP = (By.CSS_SELECTOR, ".scroll-to-top")
    
    # Form Elements (if any)
    CONTACT_FORM = (By.CSS_SELECTOR, ".contact-form")
    INQUIRY_FORM = (By.CSS_SELECTOR, ".inquiry-form")
    
    # Dynamic Locators
    @staticmethod
    def card_by_text(text):
        """Dynamic locator for card by text content"""
        return (By.XPATH, f"(//div[contains(text(), '{text}')])")
    
    @staticmethod
    def card_by_title(title):
        """Dynamic locator for card by title"""
        return (By.XPATH, f"//div[@class='card-text'][contains(text(), '{title}')]")
    
    @staticmethod
    def card_containing_text(text):
        """Dynamic locator for card containing specific text"""
        return (By.XPATH, f"//div[contains(@class, 'card')]//text()[contains(., '{text}')]/ancestor::div[contains(@class, 'card')]")
    
    @staticmethod
    def section_by_heading(heading):
        """Dynamic locator for section by heading text"""
        return (By.XPATH, f"//h2[contains(text(), '{heading}')]/parent::*")
    
    @staticmethod
    def button_by_text(button_text):
        """Dynamic locator for buttons by text"""
        return (By.XPATH, f"//button[contains(text(), '{button_text}')]")
    
    @staticmethod
    def link_by_text(link_text):
        """Dynamic locator for links by text"""
        return (By.XPATH, f"//a[contains(text(), '{link_text}')]")
    
    @staticmethod
    def card_by_index(index):
        """Dynamic locator for card by index (0-based)"""
        return (By.CSS_SELECTOR, f".card-wrapper:nth-child({index + 1})")
    
    @staticmethod
    def element_containing_text(element_type, text):
        """Dynamic locator for any element type containing specific text"""
        return (By.XPATH, f"//{element_type}[contains(text(), '{text}')]")
    
    @staticmethod
    def div_with_text(text):
        """Dynamic locator for div elements containing specific text"""
        return (By.XPATH, f"//div[contains(text(), '{text}')]")
