from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from utilities.base import search_index_by_title
from locators.retirement_wealth_page_locators import RetirementWealthPageLocators

class RetirementWealthPage:
     
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # Using centralized locators from RetirementWealthPageLocators
        self.list_cards = RetirementWealthPageLocators.CARD_FRONT_TEXT
        self.list_hover_card = RetirementWealthPageLocators.CARD_WRAPPER
        self.cards_text = RetirementWealthPageLocators.CARD_SMALL_TEXT
        self.let_start_button = RetirementWealthPageLocators.GET_STARTED_BUTTON
   

    def scroll_to_element_by_text(self, text):
        """
        Scroll to an element by its text in retirement wealth page.
        :param text: The text of the element to scroll to.
        """
        # Using dynamic locator from centralized RetirementWealthPageLocators
        element = self.driver.find_element(*RetirementWealthPageLocators.card_by_text(text))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.visibility_of(element))


    def hover_on_card(self, card_name):
        """
        Hover on a card by its name and return the text of the card.
        :param card_name: The name of the card to hover on.
        :return: The text of the card after hovering.
        """
        #List of elements with titles
        list_all_cards = self.driver.find_elements(*self.list_cards)
        #list of elements with buttons
        list_all_hover_divs = self.driver.find_elements(*self.list_hover_card)

        #Search for index for section name index
        index = search_index_by_title(list_all_cards, card_name)
        self.hover(list_all_hover_divs[index])
        card_text = self.driver.find_elements(*self.cards_text)[index].text
        return card_text

    def hover(self,element):
        """
        Hover over an element using ActionChains.
        :param element: The element to hover over.
        """
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    
    def click_let_start_button(self):
        """
        Click on the "Let's get started" button.
        """
        let_start_button = self.driver.find_element(*self.let_start_button)
        self.wait.until(EC.visibility_of(let_start_button))
        self.driver.execute_script("""arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});""", let_start_button)
        let_start_button.click()