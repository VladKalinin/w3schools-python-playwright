from abc import ABC, abstractmethod

from playwright.sync_api import Page


class BaseComponent(ABC):

    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def is_component_displayed(self): pass
