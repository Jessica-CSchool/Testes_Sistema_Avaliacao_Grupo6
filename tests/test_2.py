import pytest
from pages.customer_home_page import CustomerHomePage

class Test2:

    def test_customer_has_2plus_accounts_and_can_switch(self, setup):
        # Login como Albus Dumbledore
        home_pg = setup
        home_pg.click_customer_btn()
        home_pg.select_customer_name("Albus Dumbledore")
        home_pg.click_login_btn()

        customer_home = CustomerHomePage(home_pg.driver)
        customer_home.wait_loaded()

        # Validar que o cliente tem 2+ contas no dropdown
        accounts = customer_home.get_all_account_numbers()
        assert len(accounts) >= 2, f"Cliente deveria ter 2+ contas, mas tem {len(accounts)}: {accounts}"

        #  (Conta A)
        account_a = customer_home.get_selected_account_number()

        # Selecionando uma conta diferente 
        previous, account_b = customer_home.select_different_account()
        assert previous == account_a  

        
        selected_after = customer_home.get_selected_account_number()
        assert selected_after == account_b, f"Conta não mudou. Antes: {account_a} | Depois: {selected_after}"
        assert account_b != account_a, f"Conta selecionada deveria ser diferente. Antes: {account_a} | Nova: {account_b}"


