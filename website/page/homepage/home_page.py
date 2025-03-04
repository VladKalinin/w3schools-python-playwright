from playwright.sync_api import expect, Page
from website.page.base_page import BasePage
from website.page.component.top_navigation_header import TopNavigationHeader


class HomePage(BasePage):
    _learn_to_code_content = ".w3-center.herosection"

    def __init__(self, page: Page, base_url):
        super().__init__(page, base_url)
        self.topNavigationHeaderComponent = TopNavigationHeader(page)

    def is_current_page_opened(self):
        expect(self.page.locator(self._learn_to_code_content)).to_be_visible()
        self.get_top_navigation_header_component.is_component_displayed()

    def get_top_header_routes(self):
        return self.get_top_navigation_header_component.get_nav_header_elements()

    @property
    def get_top_navigation_header_component(self):
        return self.topNavigationHeaderComponent
