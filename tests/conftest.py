import pytest

from pages.home_page import HomePage


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')

@pytest.fixture
def setup(request):
    selected_browser = request.config.getoption('browser')
    home_pg = HomePage(browser = selected_browser)
    home_pg.open_page()
    yield home_pg  # after test
    home_pg.close()

@pytest.fixture
def run_all_browsers(all_browsers):
    home_pg = HomePage(browser = all_browsers)
    home_pg.open_page()
    yield home_pg  # after test
    home_pg.close()
