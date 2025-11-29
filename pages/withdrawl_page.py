from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WithdrawlPage(BasePage):
    amount_input = (By.CSS_SELECTOR, "input[placeholder='amount']")
    withdraw_button = (By.CSS_SELECTOR, "button[type='submit'].btn.btn-default")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def wait_loaded(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.amount_input))
        wait.until(EC.element_to_be_clickable(self.withdraw_button))
        return True

    def click_withdraw(self, timeout=10):
        self.wait_loaded(timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.withdraw_button)
        ).click()

    def get_required_validation_message(self, timeout=10) -> str:
        """
        Valida a mensagem nativa do browser para campo required.
        Ex.: PT-BR: 'Preencha este campo.'
        """
        self.wait_loaded(timeout)
        input_el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.amount_input)
        )
        # força o browser a validar e expor a validationMessage
        return self.driver.execute_script("return arguments[0].validationMessage;", input_el) or ""
