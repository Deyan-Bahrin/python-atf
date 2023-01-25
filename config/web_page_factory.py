import time
from selenium import webdriver

from config.browser import Browser
from selenium.webdriver.chrome.options import Options


class WebDriverFactory:
    IMPLICIT_WAIT_TIMEOUT = 5
    driver = None
    options = Options()
    options.add_argument('--headless')

    @staticmethod
    def get_driver(self, browser: Browser):
        if browser == Browser.FIREFOX:
            WebDriverFactory.driver = webdriver.Firefox()
        elif browser == Browser.CHROME:
            WebDriverFactory.driver = webdriver.Chrome(chrome_options=self.options)
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
