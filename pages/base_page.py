from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:

    def __init__(self, driver, browser=None):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                options_chrome = Options()
                options_chrome.add_argument('--incognito')
                self.driver = webdriver.Chrome(options=options_chrome)
                self.driver.maximize_window()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            else:
                raise Exception(f'Unknown browser: {browser}')

    def is_url(self, url):
        return self.driver.current_url == url

    def close(self ):
        self.driver.quit()