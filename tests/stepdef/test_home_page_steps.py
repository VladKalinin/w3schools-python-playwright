import pytest
from pytest_bdd import given, when, then, scenarios, parsers
from website.page.homepage.home_page import HomePage

scenarios("../features/homepage.feature")


@pytest.fixture
def home_page(page, base_url):
    return HomePage(page, base_url)


@given("Browser is on Home Page")
@then("Browser is on Home Page")
def is_on_home_page(home_page):
    home_page.is_current_page_opened()


@then(parsers.parse("following {sections} are displayed on Top Header On Home Page"))
def sections_are_displayed_on_top_header_on_home_page(home_page, sections):
    expected = [h.strip() for h in sections.split(',')]
    actual = home_page.get_top_header_routes()
    for header in expected:
        assert header in actual, f"Expected header '{header}' not found in {actual}."
