import time

from pages.bank_manager_page import BankManagerPage
from pages.customers_page import CustomersPage


class Test6:

    def test_deletar_customer(self, setup):
        #home
        home_pg = setup
        assert home_pg.is_url_home(), 'URL incorreta'
        home_pg.click_bank_btn()

        #bank manager
        bank_pg = BankManagerPage(setup.driver)
        assert bank_pg.is_url_bank_manager(), 'URL incorreta'
        bank_pg.click_customers_button_btn()

        #customers
        customers_pg = CustomersPage(setup.driver)
        assert customers_pg.is_url_customers(), 'URL incorreta'

        customers_pg.filter_customer('Ron')
        assert customers_pg.filtered_item_is_visible('Ron'), 'Customer was not found'

        customers_pg.click_delete_customer()

        customers_pg.filter_customer('Ron')
        assert customers_pg.filtered_item_is_not_visible('Ron'), 'Customer was not deleted'
