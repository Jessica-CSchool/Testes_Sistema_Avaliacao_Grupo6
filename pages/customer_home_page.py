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
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.deposit_tab))
        wait.until(EC.visibility_of_element_located(self.account_select))
        return True

    def is_tabs_visible(self, timeout=10) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(self.transactions_tab))
        wait.until(EC.visibility_of_element_located(self.deposit_tab))
        wait.until(EC.visibility_of_element_located(self.withdrawl_tab))
        return True

    def get_welcome_name(self, timeout=10) -> str:
        el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.welcome_text)
        )
        return el.text.strip()

    def get_balance(self, timeout=10) -> int:
        el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.balance_value)
        )
        return int(el.text.strip())

    # Account dropdown 
    def _get_account_select(self, timeout=10) -> Select:
        select_el = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.account_select)
        )
        return Select(select_el)

    def get_selected_account_number(self, timeout=10) -> str:
        return self._get_account_select(timeout).first_selected_option.text.strip()

    def get_all_account_numbers(self, timeout=10) -> list[str]:
        sel = self._get_account_select(timeout)
        return [opt.text.strip() for opt in sel.options if opt.text and opt.text.strip()]

    def select_account_by_visible_text(self, account_number: str, timeout=10):
        select_el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.account_select)
        )
        Select(select_el).select_by_visible_text(account_number)

        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_selected_account_number(timeout) == account_number
        )

    def select_different_account(self, timeout=10) -> tuple[str, str]:
        accounts = self.get_all_account_numbers(timeout)
        current = self.get_selected_account_number(timeout)

        other_accounts = [a for a in accounts if a != current]
        if not other_accounts:
            raise AssertionError(f"Não existe conta diferente para selecionar. Contas: {accounts}")

        new_account = other_accounts[0]
        self.select_account_by_visible_text(new_account, timeout)
        return current, new_account

    # Navegação tabs 
    def go_to_transactions(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.transactions_tab)
        ).click()
        from pages.transactions_page import TransactionsPage
        return TransactionsPage(self.driver)

    def go_to_deposit(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.deposit_tab)
        ).click()
        from pages.deposit_page import DepositPage
        return DepositPage(self.driver)

    def go_to_withdrawl(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.withdrawl_tab)
        ).click()
        from pages.withdrawl_page import WithdrawlPage
        return WithdrawlPage(self.driver)
