import pytest
from pytest_bdd import given, when, then, scenarios
from website.page.homepage.home_page import HomePage

scenarios("../features/homepage.feature")

@pytest.fixture
def home_page(page, base_url):
    return HomePage(page, base_url)

@then("Browser is on Home Page")
def user_is_on_home_page(home_page):
    home_page.is_current_page_opened()