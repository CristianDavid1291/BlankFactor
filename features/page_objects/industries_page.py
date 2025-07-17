from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utilities.base import search_index_by_title
from locators.industries_page_locators import IndustriesPageLocators

class IndustriesPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Using centralized locators from IndustriesPageLocators
        self.list_items_by_title = IndustriesPageLocators.SECTION_TITLES
        self.list_learn_more_buttons = IndustriesPageLocators.LEARN_MORE_BUTTONS
   

    def click_on_section_by_name(self, section_name):
        """
        Click on a section by its name.
        :param section_name: The name of the section to click on.
        """
        #List of elements with titles
        list_titles = self.driver.find_elements(*self.list_items_by_title)

        #list of elements with buttons
        list_learn_buttons = self.driver.find_elements(*self.list_learn_more_buttons)

        # Scroll to the element to ensure it is visible
        self.scroll_to_element_by_text(section_name)

        #Search for index for section name index
        index = search_index_by_title(list_titles, section_name)
        
        list_learn_buttons[index].click()
    
    def scroll_to_element_by_text(self, text):
        """
        Scroll to an element by its text in industries page.
        :param text: The text of the element to scroll to.
        """
        # Using dynamic locator from centralized IndustriesPageLocators
        element = self.driver.find_element(*IndustriesPageLocators.section_by_name(text))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.visibility_of(element))
    
    