from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class BankManagerPage(BasePage):
    url_bank_manager = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
    add_customer_button = (By.CSS_SELECTOR, "button[ng-click='addCust()']")
    open_account_button = (By.CSS_SELECTOR, "button[ng-click='openAccount()']")
    customers_button = (By.CSS_SELECTOR, "button[ng-click='showCust()']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url_bank_manager)

    def click_add_customer_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.add_customer_button)).click()

    def click_open_account_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.open_account_button)).click()

    def click_customers_button_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.customers_button)).click()

    def is_url_bank_manager(self):
        #return self.is_url(self.url_bank_manager)
        return self.wait.until(EC.url_contains('manager'))

