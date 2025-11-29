from pages.bank_manager_page import BankManagerPage
from pages.open_account_page import OpenAccountPage


class Test5:

    def test_abrir_nova_conta(self, setup):
        #home
        home_pg = setup
        assert home_pg.is_url_home(), 'URL incorreta'
        home_pg.click_bank_btn()

        #bank manager
        bank_pg = BankManagerPage(setup.driver)
        assert bank_pg.is_url_bank_manager(), 'URL incorreta'
        bank_pg.click_open_account_btn()

        #open account
        open_account_pg = OpenAccountPage(setup.driver)
        assert open_account_pg.is_url_open_account(), 'URL incorreta'

        open_account_pg.select_customer(option='Harry Potter')
        open_account_pg.select_currency(option='Pound')
        open_account_pg.click_process_button()

        alert_result = open_account_pg.get_alert_text()
        assert "Account created successfully" in alert_result