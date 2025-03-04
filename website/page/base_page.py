from abc import ABC, abstractmethod
from playwright.sync_api import Page


class BasePage(ABC):

    def __init__(self, page: Page, base_url):
        self.page = page
        self.base_url = base_url

    def open_page(self, path: str):
        url = f"{self.base_url}/{path}".rstrip("/")
        self.page.goto(url)

    @abstractmethod
    def is_current_page_opened(self): pass
