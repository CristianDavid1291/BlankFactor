from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class IndustriesPage(PageFactory):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.list_items_by_title = (By.CSS_SELECTOR, "div[data-type='text'] h3")
        self.list_learn_more_buttons = (By.CSS_SELECTOR, "div[data-type='text'] div.btn-wrap a")
   

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
        index = self.search_index_by_title(list_titles, section_name)
        
        list_learn_buttons[index].click()
    

    def search_index_by_title(self, titles, title):
        """
        Search for the index of a title in a list of titles.
        :param titles: List of title elements.
        :param title: The title to search for.
        :return: The index of the title if found, otherwise -1.
        """
         #Search for index for section name index
        for i in range(0,len(titles)):
            if titles[i].text == title:
                return i
        return -1
    
    def scroll_to_element_by_text(self, text):
        """
        Scroll to an element by its text in industries page.
        :param text: The text of the element to scroll to.
        """
        # Scroll to the element to ensure it is visible
        element = self.driver.find_element(By.XPATH, "(//h3[contains(text(), '"+ text +"')])")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.visibility_of(element))
    
    