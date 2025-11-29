from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WithdrawlPage(BasePage):
    amount_input = (By.CSS_SELECTOR, "input[placeholder='amount']")
    withdraw_button = (By.CSS_SELECTOR, "button[type='submit']")  # no tab Withdrawl, o submit é o Withdraw

    def __init__(self, driver):
        super().__init__(driver=driver)

    def wait_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.amount_input))
        return True

    def withdraw(self, amount: int, timeout=10):
        self.wait_loaded(timeout)
        el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.amount_input))
        el.clear()
        el.send_keys(str(amount))
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.withdraw_button)).click()
