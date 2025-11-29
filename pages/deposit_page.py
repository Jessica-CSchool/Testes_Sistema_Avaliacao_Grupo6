from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DepositPage(BasePage):
    amount_input = (By.CSS_SELECTOR, "input[placeholder='amount']")
    deposit_button = (By.CSS_SELECTOR, "button[type='submit']")  

    success_message = (By.CSS_SELECTOR, "span.error.ng-binding")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def wait_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.amount_input))
        return True

    def deposit(self, amount: int, timeout=10):
        self.wait_loaded(timeout)
        el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.amount_input))
        el.clear()
        el.send_keys(str(amount))
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.deposit_button)).click()
    
    def wait_success_message(self, expected_text="Deposit Successful", timeout=10) -> str:
        wait = WebDriverWait(self.driver, timeout)
        el = wait.until(EC.visibility_of_element_located(self.success_message))
        msg = el.text.strip()
        assert expected_text in msg, f"Mensagem inesperada. Recebido: '{msg}'"
        return msg
