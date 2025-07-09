Feature: Powering innovation in retirement services

    As a user
    I want to validate the content and functionality of the Retirement and Wealth section
    So that I can ensure the information is accurate and the links work correctly
    
Background:
    Given I am on Blank Factor home page
    
Scenario Outline: Validate AI & Machine learning content on Retirement and Wealth section
    When I navigate to the "<section_name>" section
    Then I should see the "<card_title>" displayed
    And The content with "<card_title>" should include "<content_snippet>"
    And close the browser

Examples:
    | section_name                 | card_title                   | content_snippet                                                  | 
    | Retirement and Wealth        | AI &\nMachine learning       | Automate your operations and get to market quickly and securely. |

Scenario Outline: Validate button redirection and title on Retirement and Wealth sections
    When I navigate to the "<section_name>" section
    Then I scroll down and click on get started button
    And The button should redirect to "<url>" and display the title "Contact | Blankfactor"
    And close the browser

Examples:
   | section_name             | url                                |            
   | Retirement and Wealth    | https://blankfactor.com/contact/   |  