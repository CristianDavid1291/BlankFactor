from selenium.webdriver.support.ui import WebDriverWait
class ContactPage:

    def __init__(self, driver):
        self.driver = driver
    
    def get_page_title(self):
        return self.driver.title
    
    def get_current_url(self):
        return self.driver.current_url
    
    def get_driver(self):
        return self.driver
    
    def validate_load_page(self):
        """
        Validates that the page has loaded by checking the document ready state.
        return: True if the page is loaded, False otherwise.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
            return True
        except Exception as e:
            print(f"Error while waiting for page to load: {e}")
            return False
            


    

    