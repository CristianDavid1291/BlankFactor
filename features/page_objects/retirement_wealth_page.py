from seleniumpagefactory import PageFactory
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class RetirementWealthPage:
     
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.list_cards = (By.CSS_SELECTOR, "div.card-front-inner div.card-text")
        self.list_hover_card = (By.CSS_SELECTOR, "div.card-wrapper")
        self.cards_text = (By.CSS_SELECTOR, "div.card-text.small")
        self.let_start_button = (By.LINK_TEXT, "Let's get started")
   

    def scroll_to_element_by_text(self, text):
        """
        Scroll to an element by its text in retirement wealth page.
        :param text: The text of the element to scroll to.
        """
        # Scroll to the element to ensure it is visible
        element = self.driver.find_element(By.XPATH, "(//div[contains(text(), '"+ text +"')])")
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
        index = self.search_index_by_title(list_all_cards, card_name)
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

    
    def search_index_by_title(self, titles, title):
        """
        Search for the index of a title in a list of titles.
        :param titles: List of title elements.
        :param title: The title to search for.
        :return: The index of the title if found, otherwise -1.
        """
        for i in range(0,len(titles)):
            if titles[i].text == title:
                return i
        return -1
    
    def click_let_start_button(self):
        """
        Click on the "Let's get started" button.
        """
        let_start_button = self.driver.find_element(*self.let_start_button)
        self.wait.until(EC.visibility_of(let_start_button))
        self.driver.execute_script("""arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});""", let_start_button)
        let_start_button.click()