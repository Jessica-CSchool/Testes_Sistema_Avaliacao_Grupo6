from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CustomersPage(BasePage):
    url_bank_manager_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    search_input = (By.CSS_SELECTOR, "input[placeholder='Search Customer']")
    delete_button = (By.CSS_SELECTOR, "button[ng-click='deleteCust(cust)']")
    TABLE_ROWS = (By.CSS_SELECTOR, "table.table tbody tr")
    row_filtered = (By.CSS_SELECTOR, "td")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url_bank_manager_customers)

    def filter_customer(self, customer):
        customer_filtered = self.driver.find_element(*self.search_input)
        customer_filtered.clear()
        customer_filtered.send_keys(customer)

    def click_delete_customer(self):
        self.driver.find_element(*self.delete_button).click()

    def _get_visible_rows(self):
        return self.driver.find_elements(*self.TABLE_ROWS)

    def filtered_item_is_visible(self, first_name: str) -> bool:
        rows = self._get_visible_rows()
        for row in rows:
            cols = row.find_elements(*self.row_filtered)
            if not cols:
                continue
            if cols[0].text.strip() == first_name:
                return True
        return False

    def filtered_item_is_not_visible(self, first_name: str) -> bool:
        def gone(d):
            rows = self._get_visible_rows()
            for row in rows:
                cols = row.find_elements(*self.row_filtered)
                if cols and cols[0].text.strip() == first_name:
                    return False
            return True

        WebDriverWait(self.driver, 10).until(gone)
        return True

    def is_url_customers(self):
        return self.wait.until(EC.url_contains('list'))