import time

import pytest


class Test1:

    def test_login(self, setup):
        home_pg = setup
        home_pg.click_customer_btn()
        time.sleep(4)