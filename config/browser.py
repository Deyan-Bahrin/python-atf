from enum import Enum


class Browser(Enum):
    IE10 = "ie10"
    CHROME = "chrome"
    FIREFOX = "firefox"
    SAFARI = "safari"
    browserName = str()

    def __init__(self, browserName):
        self.browserName = browserName

    def getBrowserName(self):
        return self.browserName

