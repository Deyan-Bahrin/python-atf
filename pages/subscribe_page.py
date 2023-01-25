from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SubscribePage(BasePage):
    weekend_page = "//*[@id='site-content']/div[2]/div/div[2]/section/a[3]"

    def __init__(self, driver):
        super().__init__(driver)
        self.weekend_page = driver.find_element(By.XPATH, self.weekend_page)

    def click_on_weekend_button(self):
        self.weekend_page.click()
