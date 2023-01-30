from config.browser import Browser
from config.web_page_factory import WebDriverFactory
from pages.base_page import BasePage
from pages.home_page import FtHomePage
import allure


class Tests:
    base_url = BasePage.init_config()
    driver = WebDriverFactory.get_driver(Browser.CHROME)

    @allure.step("test")
    def test_hello(self):
        self.driver.get(self.base_url)
        home_pages = FtHomePage(self.driver)
        subscribe_page = home_pages.click_on_subscribe_button()
        subscribe_page.click_on_weekend_button()
