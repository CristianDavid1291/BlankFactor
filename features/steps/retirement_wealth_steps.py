from behave import *
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utilities.base as base
from page_objects.home_page import HomePage


@given(u'I am on Blank Factor home page')
def launch_browser(context):
    context.driver = base.setup_driver()
    context.home_page = HomePage(context.driver)
    context.home_page.accept_cookies()
    context.home_page.click_on_header_navigation_link("Industries")
    