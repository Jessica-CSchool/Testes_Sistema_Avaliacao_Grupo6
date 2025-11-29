from pages.bank_manager_page import BankManagerPage
from pages.add_customer_page import AddCustomerPage

class Test4:

    def test_criar_novo_customer(self, setup):
        #home
        home_pg = setup
        assert home_pg.is_url_home(), 'URL incorreta'
        home_pg.click_bank_btn()

        #bank manager
        bank_pg = BankManagerPage(setup.driver)
        assert bank_pg.is_url_bank_manager(), 'URL incorreta'
        bank_pg.click_add_customer_btn()

        #add customer form
        add_customer_pg = AddCustomerPage(setup.driver)
        assert add_customer_pg.is_url_add_customer(), 'URL incorreta'
        add_customer_pg.input_form_add_customer_data('Draco','Malfoy','99999')

        #success alert message
        alert_result = add_customer_pg.get_alert_text()
        assert "Customer added successfully" in alert_result