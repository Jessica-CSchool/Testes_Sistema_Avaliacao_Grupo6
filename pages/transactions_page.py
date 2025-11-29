from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransactionsPage(BasePage):
    table = (By.CSS_SELECTOR, "table.table")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def wait_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.table))
        return True
