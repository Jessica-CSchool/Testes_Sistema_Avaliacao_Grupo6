from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    url_home = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    customer_button = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    bank_button = (By.CSS_SELECTOR, "button[ng-click='manager()']")

    def __init__(self, browser='chrome'):
        super().__init__(driver=None, browser=browser)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url_home)

    def click_customer_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.customer_button)).click()

    def click_bank_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.bank_button)).click()

    def is_url_home(self):
        return self.is_url(self.url_home)
