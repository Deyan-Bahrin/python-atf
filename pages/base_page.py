from configparser import ConfigParser

from selenium.common.exceptions import TimeoutException as time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.init_config()

    def get_driver(self):
        if self.driver:
            return self.driver
        else:
            raise Exception("Driver has not been initialized.")

    @staticmethod
    def wait_for_seconds(timeout_in_second):
        try:
            time.sleep(timeout_in_second)
        except InterruptedError as e:
            print(e)

    @staticmethod
    def init_config():
        config = ConfigParser()
        config.read("/Users/deyan/Documents/python-atf/python-atf/config/test_properties.ini")
        return config.get("base", "browser_url")
