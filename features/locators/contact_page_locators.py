"""
Contact Page Locators
Contains all locators specific to the Contact Page
"""

from selenium.webdriver.common.by import By


class ContactPageLocators:
    """Locators for Contact Page elements"""
    
    # Page Structure
    PAGE_TITLE = (By.CSS_SELECTOR, "h1.page-title")
    PAGE_HEADING = (By.CSS_SELECTOR, "h1")
    PAGE_DESCRIPTION = (By.CSS_SELECTOR, ".page-description")
    BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb")
    
    # Contact Form
    CONTACT_FORM = (By.CSS_SELECTOR, "form.contact-form")
    FORM_CONTAINER = (By.CSS_SELECTOR, ".form-container")
    FORM_TITLE = (By.CSS_SELECTOR, ".form-title")
    
    # Form Fields
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    FULL_NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PHONE_INPUT = (By.ID, "phone")
    COMPANY_INPUT = (By.ID, "company")
    JOB_TITLE_INPUT = (By.ID, "jobTitle")
    MESSAGE_TEXTAREA = (By.ID, "message")
    SUBJECT_INPUT = (By.ID, "subject")
    
    # Form Labels
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, "label[for='firstName']")
    LAST_NAME_LABEL = (By.CSS_SELECTOR, "label[for='lastName']")
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email']")
    PHONE_LABEL = (By.CSS_SELECTOR, "label[for='phone']")
    MESSAGE_LABEL = (By.CSS_SELECTOR, "label[for='message']")
    
    # Form Buttons
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEND_BUTTON = (By.CSS_SELECTOR, ".send-btn")
    RESET_BUTTON = (By.CSS_SELECTOR, "button[type='reset']")
    CLEAR_BUTTON = (By.CSS_SELECTOR, ".clear-btn")
    CANCEL_BUTTON = (By.CSS_SELECTOR, ".cancel-btn")
    
    # Form Validation
    REQUIRED_FIELD_ERROR = (By.CSS_SELECTOR, ".field-error")
    EMAIL_VALIDATION_ERROR = (By.CSS_SELECTOR, ".email-error")
    PHONE_VALIDATION_ERROR = (By.CSS_SELECTOR, ".phone-error")
    FORM_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".success-message")
    FORM_ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    VALIDATION_MESSAGE = (By.CSS_SELECTOR, ".validation-message")
    
    # Contact Information Section
    CONTACT_INFO_SECTION = (By.CSS_SELECTOR, ".contact-info")
    OFFICE_ADDRESS = (By.CSS_SELECTOR, ".office-address")
    MAILING_ADDRESS = (By.CSS_SELECTOR, ".mailing-address")
    PHONE_NUMBER = (By.CSS_SELECTOR, ".phone-number")
    EMAIL_ADDRESS = (By.CSS_SELECTOR, ".email-address")
    BUSINESS_HOURS = (By.CSS_SELECTOR, ".business-hours")
    
    # Office Locations
    HEADQUARTERS = (By.CSS_SELECTOR, ".headquarters")
    BRANCH_OFFICES = (By.CSS_SELECTOR, ".branch-offices")
    REGIONAL_OFFICES = (By.CSS_SELECTOR, ".regional-offices")
    
    # Social Media Links
    SOCIAL_MEDIA_SECTION = (By.CSS_SELECTOR, ".social-media")
    LINKEDIN_LINK = (By.CSS_SELECTOR, "a[href*='linkedin']")
    TWITTER_LINK = (By.CSS_SELECTOR, "a[href*='twitter']")
    FACEBOOK_LINK = (By.CSS_SELECTOR, "a[href*='facebook']")
    YOUTUBE_LINK = (By.CSS_SELECTOR, "a[href*='youtube']")
    INSTAGRAM_LINK = (By.CSS_SELECTOR, "a[href*='instagram']")
    
    # Map/Location Elements
    MAP_CONTAINER = (By.CSS_SELECTOR, ".map-container")
    MAP_IFRAME = (By.CSS_SELECTOR, "iframe[src*='maps']")
    LOCATION_MARKER = (By.CSS_SELECTOR, ".location-marker")
    
    # Additional Contact Options
    LIVE_CHAT_BUTTON = (By.CSS_SELECTOR, ".live-chat-btn")
    CALLBACK_REQUEST = (By.CSS_SELECTOR, ".callback-request")
    APPOINTMENT_BOOKING = (By.CSS_SELECTOR, ".appointment-booking")
    
    # Dynamic Locators
    @staticmethod
    def form_field_by_name(field_name):
        """Dynamic locator for form fields by name attribute"""
        return (By.NAME, field_name)
    
    @staticmethod
    def form_field_by_id(field_id):
        """Dynamic locator for form fields by ID"""
        return (By.ID, field_id)
    
    @staticmethod
    def form_field_by_label(label_text):
        """Dynamic locator for form fields by label text"""
        return (By.XPATH, f"//label[contains(text(), '{label_text}')]/following-sibling::input")
    
    @staticmethod
    def label_by_text(label_text):
        """Dynamic locator for labels by text"""
        return (By.XPATH, f"//label[contains(text(), '{label_text}')]")
    
    @staticmethod
    def error_message_for_field(field_name):
        """Dynamic locator for field-specific error messages"""
        return (By.CSS_SELECTOR, f".{field_name}-error")
    
    @staticmethod
    def input_with_placeholder(placeholder_text):
        """Dynamic locator for inputs by placeholder text"""
        return (By.XPATH, f"//input[@placeholder='{placeholder_text}']")
    
    @staticmethod
    def social_link_by_platform(platform):
        """Dynamic locator for social media links by platform"""
        return (By.CSS_SELECTOR, f"a[href*='{platform.lower()}']")
    
    @staticmethod
    def button_by_text(button_text):
        """Dynamic locator for buttons by text"""
        return (By.XPATH, f"//button[contains(text(), '{button_text}')]")
    
    @staticmethod
    def heading_by_text(heading_text):
        """Dynamic locator for headings by text"""
        return (By.XPATH, f"//*[self::h1 or self::h2 or self::h3][contains(text(), '{heading_text}')]")
