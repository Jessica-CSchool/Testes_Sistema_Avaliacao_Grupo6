from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class AddCustomerPage(BasePage):
    url_bank_manager_add_customer = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust'
    add_customer_submit_button = (By.CSS_SELECTOR, "button[type='submit']")
    first_name_input = (By.CSS_SELECTOR, "input[placeholder='First Name']")
    last_name_input = (By.CSS_SELECTOR, "input[placeholder='Last Name']")
    post_code_input= (By.CSS_SELECTOR, "input[placeholder='Post Code']")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url_bank_manager_add_customer)

    def click_add_customer_submit_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.add_customer_submit_button)).click()

    def input_form_add_customer_data(self, firstname,lastname,postcode): #optional parameters
        self.driver.find_element(*self.first_name_input).send_keys(firstname)
        self.driver.find_element(*self.last_name_input).send_keys(lastname)
        self.driver.find_element(*self.post_code_input).send_keys(postcode)
        self.click_add_customer_submit_btn()

    def is_url_add_customer(self):
        #return self.is_url(self.url_bank_manager_add_customer)
        return self.wait.until(EC.url_contains('addCust'))

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        texto_alerta = alert.text
        alert.accept()
        return texto_alerta
