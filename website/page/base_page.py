from abc import ABC, abstractmethod

from website.base_component import BaseComponent

class BasePage(BaseComponent):

    def __init__(self, page, base_url):
        super().__init__(page)
        self.base_url = base_url

    def open_page(self, path: str):
        url = f"{self.base_url}/{path}".rstrip("/")
        self.page.goto(url)

    @abstractmethod
    def is_current_page_opened(self): pass
