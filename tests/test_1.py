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

        assert customer_home.get_welcome_name() == "Albus Dumbledore"
        assert customer_home.is_tabs_visible() is True
        assert customer_home.get_selected_account_number() != ""
        assert customer_home.get_balance() >= 0
