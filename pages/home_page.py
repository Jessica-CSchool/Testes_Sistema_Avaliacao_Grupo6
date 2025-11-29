<<<<<<< Updated upstream
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
=======
from pages.base_page import BasePage

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

>>>>>>> Stashed changes

class HomePage(BasePage):
    url_home = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    customer_button = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    bank_button = (By.CSS_SELECTOR, "button[ng-click='manager()']")


    user_select = (By.ID, "userSelect")
    login_button = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, browser='chrome'):
        super().__init__(driver=None, browser=browser)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get(self.url_home)

    def click_customer_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.customer_button)).click()

    def click_bank_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.bank_button)).click()

    def is_url_home(self):
        return self.is_url(self.url_home)

    #Selecionar customer no dropdown
    def select_customer_name(self, customer_name: str):
        wait = WebDriverWait(self.driver, 10)
        dropdown = wait.until(EC.element_to_be_clickable(self.user_select))
        Select(dropdown).select_by_visible_text(customer_name)

    # clicar no botão Login após selecionar
    def click_login_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.login_button)).click()
