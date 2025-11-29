import pytest
import time
from pages.customer_home_page import CustomerHomePage

class Test3:

    def test_withdraw_required_amount_shows_browser_message(self, setup):
        # Login como Albus Dumbledore
        home_pg = setup
        home_pg.click_customer_btn()
        home_pg.select_customer_name("Albus Dumbledore")
        home_pg.click_login_btn()

        customer_home = CustomerHomePage(home_pg.driver)
        customer_home.wait_loaded()

        # Indo para o botão Withdrawl
        withdraw_page = customer_home.go_to_withdrawl()

        # Não preencher o campo amount e clicar no botão Withdraw
        withdraw_page.click_withdraw()

        msg = withdraw_page.get_required_validation_message()


        assert "Preencha este campo" in msg, f"Mensagem esperada não encontrada. Recebido: '{msg}'"
