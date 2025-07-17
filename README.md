# BlankFactor Test Automation Framework

This is a comprehensive test automation framework for validating the BlankFactor website functionality, specifically focusing on the Retirement and Wealth section validation using Selenium WebDriver and Behave (BDD).

## Project Structure

```
BlankFactor/
├── README.md
├── requirements.txt
├── features/
│   ├── blank_factor.feature          # BDD feature file with test scenarios
│   ├── environment.py                # Behave environment configuration
│   ├── data/
│   │   ├── config.ini                # Configuration file for test settings
│   │   ├── data.py                   # Test data configuration
│   │   └── __pycache__/
│   ├── locators/                     # Centralized Locator Management
│   │   ├── __init__.py               # Package initialization for clean imports
│   │   ├── home_page_locators.py     # Home page element locators
│   │   ├── industries_page_locators.py # Industries page element locators
│   │   ├── retirement_wealth_page_locators.py # Retirement wealth page locators
│   │   ├── contact_page_locators.py  # Contact page element locators
│   │   └── README.md                 # Locator management documentation
│   ├── page_objects/
│   │   ├── contact_page.py           # Contact page object model
│   │   ├── home_page.py              # Home page object model
│   │   ├── industries_page.py        # Industries page object model
│   │   └── retirement_wealth_page.py # Retirement wealth page object model
│   ├── steps/
│   │   ├── retirement_wealth_steps.py # Step definitions for BDD scenarios
│   │   └── __pycache__/
│   └── utilities/
│       ├── base.py                   # Base utility functions for driver management
│       ├── custom_logger.py          # Custom logging configuration
│       ├── read_properties.py        # Configuration file reader utility
│       └── __pycache__/
├── logs/
│   └── automation.log                # Test execution logs
└── manual_testing/
    ├── WebApplication_TestPlan.docx  # Manual test plan document
    └── WebApplication_TestPlan.xlsx  # Manual test plan spreadsheet
```

## Features

- **BDD Testing**: Uses Behave framework for behavior-driven development
- **Page Object Model**: Implements page object pattern for maintainable code
- **Centralized Locator Management**: Individual locator files for each page for better organization
- **Selenium WebDriver**: Automated browser testing with Chrome driver
- **Allure Reporting**: Comprehensive test reporting with Allure framework
- **Configuration Management**: External configuration files for test settings
- **Cross-browser Support**: Configurable for different browsers
- **Data-driven Testing**: Supports parameterized test scenarios
- **Custom Logging**: Integrated logging system for test execution tracking
- **Manual Testing Documentation**: Includes comprehensive manual test plans and documentation

## Testing Strategy

This framework supports both automated and manual testing approaches with advanced architecture:

### Automated Testing
- **BDD Framework**: Behavior-driven development using Gherkin syntax
- **Page Object Model**: Structured page representation with centralized locators
- **Centralized Locator Management**: Individual locator files per page for better maintainability
- **Dynamic Locators**: Support for parameterized element identification
- **Continuous Integration**: Ready for CI/CD pipeline integration
- **Cross-browser Testing**: Configurable for different browsers
- **Configuration-driven**: External configuration for flexible test environment management

### Manual Testing
- **Test Plans**: Comprehensive manual test plans in multiple formats
- **Documentation**: Detailed test cases and scenarios
- **Hybrid Approach**: Combines automated and manual testing strategies

## Architecture Highlights

### Centralized Locator Management
The framework implements a sophisticated locator management system with individual files for each page:

- **Individual Locator Files**: Each page has its own locator file for better organization
- **Static Locators**: Pre-defined element locators for common page elements
- **Dynamic Locators**: Parameterized locators using `@staticmethod` for flexible element identification
- **Package Structure**: Clean import system through `__init__.py` for easy access

```python
# Example usage
from locators import HomePageLocators, ContactPageLocators

# Static locator
self.driver.find_element(*HomePageLocators.ACCEPT_COOKIES_BUTTON).click()

# Dynamic locator
section_locator = IndustriesPageLocators.section_by_name("Retirement and Wealth")
element = self.driver.find_element(*section_locator)
```

### Configuration Management
- **External Configuration**: `config.ini` for environment-specific settings
- **Data Separation**: Test data separated from test logic in dedicated files
- **Properties Reader**: Utility class for reading configuration properties

## Test Scenarios

### Current Test Coverage:

1. **AI & Machine Learning Content Validation**
   - Validates content display in Retirement and Wealth section
   - Verifies specific content snippets are present

2. **Button Redirection Validation**
   - Tests "Get Started" button functionality
   - Validates URL redirection to contact page
   - Verifies page title after navigation

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.7+
- Chrome Browser
- ChromeDriver (automatically managed by Selenium)
- Git (for version control)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd BlankFactor
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Allure (for reporting):**
   
   **Windows (using Scoop):**
   ```bash
   scoop install allure
   ```
   
   **macOS (using Homebrew):**
   ```bash
   brew install allure
   ```
   
   **Linux:**
   ```bash
   # Download and install from https://github.com/allure-framework/allure2/releases
   ```

## Running Tests

### Basic Test Execution

1. **Run all tests:**
   ```bash
   behave
   ```

2. **Run specific feature:**
   ```bash
   behave features/blank_factor.feature
   ```

3. **Run with specific tags (if implemented):**
   ```bash
   behave --tags=@smoke
   ```

### Running Tests with Allure Reporting

1. **Run tests and generate Allure results:**
   ```bash
   behave -f allure_behave.formatter:AllureFormatter -o allure-results
   ```

2. **Generate and serve Allure report:**
   ```bash
   allure serve allure-results
   ```

3. **Generate static Allure report:**
   ```bash
   allure generate allure-results -o allure-report --clean
   ```

### Advanced Test Execution

1. **Run tests with verbose output:**
   ```bash
   behave --verbose
   ```

2. **Run tests with custom format:**
   ```bash
   behave --format=pretty
   ```

3. **Run tests and capture stdout:**
   ```bash
   behave --capture
   ```

## Configuration

### Test Configuration Files

The framework uses multiple configuration approaches for maximum flexibility:

#### 1. Configuration File (`features/data/config.ini`)
```ini
[common]
base_url = https://blankfactor.com/
implicit_wait = 10
```

#### 2. Data Configuration (`features/data/data.py`)
```python
data = {
    "qa_url": "https://blankfactor.com/",
    "implicit_wait": 10,
}
```

#### 3. Properties Reader (`features/utilities/read_properties.py`)
Utility class to read configuration values:
```python
from utilities.read_properties import ReadConfig

# Get URL from config file
url = ReadConfig.get_app_url()
wait_time = ReadConfig.get_implicit_wait()
```

### Browser Configuration

The framework currently uses Chrome browser by default. To modify browser settings, update the `setup_driver()` function in `features/utilities/base.py`.

### Locator Configuration

Locators are organized in individual files under `features/locators/`:
- `home_page_locators.py` - Home page elements
- `industries_page_locators.py` - Industries page elements  
- `retirement_wealth_page_locators.py` - Retirement wealth page elements
- `contact_page_locators.py` - Contact page elements

## Reporting

### Allure Reports

The framework supports comprehensive Allure reporting with the following features:

- **Test Results**: Pass/Fail status with detailed logs
- **Screenshots**: Automatic screenshot capture on failures (when implemented)
- **Step Details**: Detailed step execution information
- **Test Duration**: Execution time tracking
- **Historical Data**: Trend analysis across test runs

### Report Structure

- **Overview**: Summary of test execution
- **Categories**: Test categorization and filtering
- **Suites**: Test suite organization
- **Graphs**: Visual representation of test results
- **Timeline**: Test execution timeline

### Logging System

The framework includes a custom logging system:

- **Automatic Logging**: Test execution logs stored in `logs/automation.log`
- **Custom Logger**: Configurable logging levels and formats
- **Error Tracking**: Detailed error logging for debugging

## Best Practices

### Framework Architecture
- Follow Page Object Model pattern with centralized locators
- Use individual locator files for each page for better organization
- Implement dynamic locators for flexible element identification
- Separate test data from test logic using configuration files

### Test Development
- Use descriptive test names and scenarios in Gherkin format
- Implement proper error handling with try-catch blocks
- Add appropriate waits for dynamic content (WebDriverWait)
- Write reusable utility functions in the utilities package

### Locator Management
- Define locators in centralized locator files
- Use static locators for fixed elements
- Implement dynamic locators using `@staticmethod` for parameterized elements
- Group related locators together in logical sections

### Configuration Management
- Use external configuration files for environment-specific settings
- Separate test data from test configuration
- Implement configuration readers for easy property access

## Framework Evolution & Recent Improvements

### Version 2.0 Updates

#### 🎯 Centralized Locator Management
- **Individual Locator Files**: Implemented separate locator files for each page
- **Dynamic Locators**: Added support for parameterized element identification
- **Clean Imports**: Package structure with `__init__.py` for simplified imports
- **Better Organization**: Logical grouping of locators by functionality

#### ⚙️ Enhanced Configuration Management
- **Multiple Config Sources**: Support for both `.ini` files and Python dictionaries
- **Properties Reader**: Utility class for reading configuration values
- **Environment Flexibility**: Easy switching between different test environments

#### 🔧 Improved Utilities
- **Bug Fixes**: Fixed search algorithm in `base.py` utilities
- **Enhanced Functions**: Added page title and URL getter methods
- **Better Error Handling**: Improved exception handling across the framework

#### 📝 Documentation
- **Comprehensive Guides**: Detailed documentation for locator management
- **Usage Examples**: Code samples for different implementation approaches
- **Best Practices**: Guidelines for maintaining the framework

## File Organization Benefits

### Before Centralization
```python
# Scattered locators across files
(By.XPATH, "//button[contains(text(), 'Accept All')]")  # In multiple files
```

### After Centralization
```python
# Organized, reusable locators
from locators import HomePageLocators
HomePageLocators.ACCEPT_COOKIES_BUTTON  # Single source of truth
```

### Maintainability Improvements
- ✅ **Single Source of Truth**: Each locator defined once
- ✅ **Easy Updates**: Change UI locators in one place
- ✅ **Better Testing**: Centralized locators are easier to validate
- ✅ **Team Collaboration**: Clear separation of concerns
- ✅ **Code Reusability**: Share locators across test files