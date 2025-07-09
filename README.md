# BlankFactor Test Automation Framework

This is a comprehensive test automation framework for validating the BlankFactor website functionality, specifically focusing on the Retirement and Wealth section validation using Selenium WebDriver and Behave (BDD).

## Project Structure

```
BlankFactor/
├── README.md
├── requirements.txt
├── features/
│   ├── blank_factor.feature          # BDD feature file with test scenarios
│   ├── data/
│   │   ├── data.py                   # Test data configuration
│   │   └── __pycache__/
│   ├── page_objects/
│   │   ├── contact_page.py           # Contact page object model
│   │   ├── home_page.py              # Home page object model
│   │   ├── industries_page.py        # Industries page object model
│   │   ├── retirement_wealth_page.py # Retirement wealth page object model
│   │   └── __pycache__/
│   ├── steps/
│   │   ├── retirement_wealth_steps.py # Step definitions for BDD scenarios
│   │   └── __pycache__/
│   └── utilities/
│       ├── base.py                   # Base utility functions for driver management
│       └── __pycache__/
└── manual_testing/
    ├── WebApplication_TestPlan.docx  # Manual test plan document
    └── WebApplication_TestPlan.xlsx  # Manual test plan spreadsheet
```

## Features

- **BDD Testing**: Uses Behave framework for behavior-driven development
- **Page Object Model**: Implements page object pattern for maintainable code
- **Selenium WebDriver**: Automated browser testing with Chrome driver
- **Allure Reporting**: Comprehensive test reporting with Allure framework
- **Cross-browser Support**: Configurable for different browsers
- **Data-driven Testing**: Supports parameterized test scenarios
- **Manual Testing Documentation**: Includes comprehensive manual test plans and documentation

## Testing Strategy

This framework supports both automated and manual testing approaches:

### Automated Testing
- **BDD Framework**: Behavior-driven development using Gherkin syntax
- **Continuous Integration**: Ready for CI/CD pipeline integration
- **Cross-browser Testing**: Configurable for different browsers

### Manual Testing
- **Test Plans**: Comprehensive manual test plans in multiple formats
- **Documentation**: Detailed test cases and scenarios

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

### Test Data Configuration

Edit `features/data/data.py` to modify test configuration:

```python
data = {
    "qa_url": "https://blankfactor.com/",
    "implicit_wait": 10,
}
```

### Browser Configuration

The framework currently uses Chrome browser by default. To modify browser settings, update the `setup_driver()` function in `features/utilities/base.py`.

## Reporting

### Report Structure

- **Overview**: Summary of test execution
- **Categories**: Test categorization and filtering
- **Suites**: Test suite organization
- **Graphs**: Visual representation of test results
- **Timeline**: Test execution timeline

## Best Practices

- Follow Page Object Model pattern
- Use descriptive test names and scenarios
- Implement proper error handling
- Add appropriate waits for dynamic content
- Keep test data separate from test logic
- Write reusable utility functions