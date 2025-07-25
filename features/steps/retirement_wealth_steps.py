from behave import *
from selenium import webdriver
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from page_objects.home_page import HomePage
from page_objects.industries_page import IndustriesPage
from page_objects.retirement_wealth_page import RetirementWealthPage
from page_objects.contact_page import ContactPage
import utilities.base as base
from utilities.custom_logger import LogGen


logger = LogGen.log_gentest()

@given(u'I am on Blank Factor home page')
def launch_browser(context):
    context.logger = logger
    context.driver = base.setup_driver()
    context.logger.info("***********Browser launched successfully.***********")
    context.home_page = HomePage(context.driver)
    context.home_page.accept_cookies()
    context.home_page.click_on_header_navigation_link("Industries")


@when(u'I navigate to the "{section_name}" section')
def navigate_section(context, section_name):
    context.industries_page = IndustriesPage(context.driver)
    context.industries_page.click_on_section_by_name(section_name)
    context.retirement_wealth_page = RetirementWealthPage(context.driver)

    
@then(u'I should see the "{card_title}" displayed')
def validate_cards(context, card_title):
    context.retirement_wealth_page.scroll_to_element_by_text(card_title.split()[0])


@then(u'The content with "{card_title}" should include "{content_snippet}"')
def validate_section_content(context, card_title, content_snippet):
 #validate the content snippet is present in the card text
 assert content_snippet in context.retirement_wealth_page.hover_on_card(card_title), f"Expected content snippet '{content_snippet}' not found in card text."


@then(u'close the browser')
def close_browser(context):
    #base.close_driver(context.driver)
    pass

 
@then(u'I scroll down and click on get started button')
def validate_let_started(context):
   context.retirement_wealth_page.click_let_start_button()


@then(u'The button should redirect to "{url}" and display the title "{title}"')
def step_impl(context, url, title):
    contact_page = ContactPage(context.driver)
    assert contact_page.validate_load_page(), "Page did not load successfully."
    current_url = context.driver.current_url
    current_title = context.driver.title
    assert current_url == url, f"Expected URL '{url}' but got '{current_url}'"
    assert current_title == title, f"Expected title '{title}' but got '{current_title}'"
    print(f"Successfully navigated with title '{current_title}'")
    
    
    



    