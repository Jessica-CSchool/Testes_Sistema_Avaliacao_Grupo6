import pytest
from pages.customer_home_page import CustomerHomePage


class Test1:

    def test_login(self, setup):
        home_pg = setup
        home_pg.click_customer_btn()
        home_pg.select_customer_name("Albus Dumbledore")
        home_pg.click_login_btn()

        customer_home = CustomerHomePage(home_pg.driver)
        customer_home.wait_loaded()

        balance_before = customer_home.get_balance()

        deposit_page = customer_home.go_to_deposit()
        deposit_amount = 10
        deposit_page.deposit(deposit_amount)

        deposit_page.wait_success_message("Deposit Successful")

        balance_after = customer_home.get_balance()

        assert balance_after > balance_before, f"Balance não aumentou. Antes: {balance_before} | Depois: {balance_after}"


        


   
