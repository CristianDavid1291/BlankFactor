"""
Locators Package
Centralized locator management for BlankFactor test framework
"""

from .home_page_locators import HomePageLocators
from .industries_page_locators import IndustriesPageLocators
from .retirement_wealth_page_locators import RetirementWealthPageLocators
from .contact_page_locators import ContactPageLocators

__all__ = [
    'HomePageLocators', 
    'IndustriesPageLocators',
    'RetirementWealthPageLocators',
    'ContactPageLocators'
]
