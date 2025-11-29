from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class CustomerHomePage(BasePage):

    
    welcome_text = (By.CSS_SELECTOR, "span.fontBig.ng-binding")  

    transactions_tab = (By.CSS_SELECTOR, "button[ng-click='transactions()']")
    deposit_tab = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
    withdrawl_tab = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")

    account_select = (By.ID, "accountSelect")

    
    balance_value = (By.CSS_SELECTOR, "div.center strong.ng-binding:nth-of-type(2)")

    def __init__(self, driver):
        super().__init__(driver=driver)

    def wait_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.deposit_tab))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.account_select))
        return True

    def get_welcome_name(self, timeout=10) -> str:
        el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.welcome_text))
        return el.text.strip()

    def get_balance(self, timeout=10) -> int:
        el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.balance_value))
        return int(el.text.strip())

    def get_selected_account_number(self, timeout=10) -> str:
        select_el = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(self.account_select))
        return Select(select_el).first_selected_option.text.strip()

    def select_account_by_visible_text(self, account_number: str, timeout=10):
        select_el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.account_select))
        Select(select_el).select_by_visible_text(account_number)

    def go_to_transactions(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.transactions_tab)).click()
        from pages.transactions_page import TransactionsPage
        return TransactionsPage(self.driver)

    def go_to_deposit(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.deposit_tab)).click()
        from pages.deposit_page import DepositPage
        return DepositPage(self.driver)

    def go_to_withdrawl(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self.withdrawl_tab)).click()
        from pages.withdrawl_page import WithdrawlPage
        return WithdrawlPage(self.driver)
