import time
from selenium import webdriver

from config.browser import Browser


class WebDriverFactory:
    IMPLICIT_WAIT_TIMEOUT = 5
    driver = None

    @staticmethod
    def get_driver(browser: Browser):
        if browser == Browser.FIREFOX:
            WebDriverFactory.driver = webdriver.Firefox()
        elif browser == Browser.CHROME:
            WebDriverFactory.driver = webdriver.Chrome()
        elif browser == Browser.IE10:
            WebDriverFactory.driver = webdriver.Ie()
        elif browser == Browser.SAFARI:
            WebDriverFactory.driver = webdriver.Safari()
        else:
            raise Exception("Unsupported browser type")

        WebDriverFactory.driver.implicitly_wait(WebDriverFactory.IMPLICIT_WAIT_TIMEOUT)
        WebDriverFactory.driver.maximize_window()
        return WebDriverFactory.driver

    @staticmethod
    def finish_test():
        if WebDriverFactory.driver:
            WebDriverFactory.driver.quit()
            WebDriverFactory.driver = None
