from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class CustomersPage(BasePage):
    url_bank_manager_customers = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list'
    search_input = (By.CSS_SELECTOR, "input[placeholder='Search Customer']")
    delete_button = (By.CSS_SELECTOR, "button[ng-click='deleteCust(cust)']")
    #filtered_td_item = (By.CSS_SELECTOR, "input[placeholder='Filter Customers']")

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

    def filtered_item_is_visible(self,customer):
        xpath_table = f"//tbody//td[normalize-space()='{customer}']"
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath_table)))
            return True
        except:
            return False

    def filtered_item_is_not_visible(self,customer):
        xpath_table = f"//tbody//td[normalize-space()='{customer}']"
        try:
            self.wait.until(EC.invisibility_of_element_located((By.XPATH, xpath_table)))
            return True
        except:
            return False

    def is_url_customers(self):
        #return self.is_url(self.url_bank_manager_add_customer)
        return self.wait.until(EC.url_contains('list'))