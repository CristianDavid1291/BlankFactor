from selenium import webdriver


def after_scenario(context, scenario):
    """
    Hook that runs AFTER each scenario.
    Here the browser is closed.
    """
    if context.driver is not None:
        context.driver.quit()
        context.logger.info("Browser closed successfully after scenario execution.")
        
