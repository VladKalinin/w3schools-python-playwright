import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright, expect
from website.page.homepage.home_page import HomePage

env = os.getenv("ENV")
env_file = f"env/.env.{env}"

if os.path.exists(env_file):
    load_dotenv(env_file)
else:
    raise FileNotFoundError(f"Environment file '{env_file}' not found!")

expect.set_options(timeout=5_000)


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser, base_url):
    context = browser.new_context()
    page = context.new_page()
    home_page = HomePage(page, base_url)
    home_page.open_page("")
    yield page
    page.close()
