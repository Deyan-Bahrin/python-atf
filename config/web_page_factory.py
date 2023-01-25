import time
from selenium import webdriver

from config.browser import Browser
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:
    IMPLICIT_WAIT_TIMEOUT = 5
    driver = None


    @staticmethod
    def get_driver(browser: Browser):
        if browser == Browser.FIREFOX:
            WebDriverFactory.driver = webdriver.Firefox()
        elif browser == Browser.CHROME:
            options = Options()
            options.add_argument('--headless')
            WebDriverFactory.driver = webdriver.Chrome('drivers/chromedriver',chrome_options=options)
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
