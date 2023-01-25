from pages.base_page import BasePage
from selenium.webdriver.common.by import By

from pages.subscribe_page import SubscribePage


class FtHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.subscribe_button = driver.find_element(By.XPATH, "//*[@id='site-navigation']/div[2]/div/div/div[3]/a[1]")

    def click_on_subscribe_button(self):
        self.subscribe_button.click()
        return SubscribePage(self.driver)
