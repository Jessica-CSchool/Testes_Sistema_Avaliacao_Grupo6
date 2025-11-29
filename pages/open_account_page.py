from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class OpenAccountPage(BasePage):
    url_bank_manager_open_account = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/openAccount'
    process_button = (By.CSS_SELECTOR, "button[type='submit']")
    select_customer_name_option = (By.ID, "userSelect")
    select_currency_option = (By.ID, "currency")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url_bank_manager_open_account)

    def click_process_button(self):
        self.wait.until(EC.element_to_be_clickable(self.process_button)).click()

    def select_customer(self, option):
        element = self.wait.until(EC.visibility_of_element_located(self.select_customer_name_option))
        dropdown = Select(element)
        dropdown.select_by_visible_text(option)

    def select_currency(self, option):
        element = self.wait.until(EC.visibility_of_element_located(self.select_currency_option))
        dropdown = Select(element)
        dropdown.select_by_visible_text(option)

    def is_url_open_account(self):
        #return self.is_url(self.url_bank_manager_open_account)
        return self.wait.until(EC.url_contains('openAccount'))

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        texto_alerta = alert.text
        alert.accept()
        return texto_alerta