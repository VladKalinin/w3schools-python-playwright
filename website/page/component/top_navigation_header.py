from playwright.sync_api import expect

from website.base_component import BaseComponent


class TopNavigationHeader(BaseComponent):
    _top_nav_bar_section = "#top-nav-bar"
    _top_nav_header_elements = f"{_top_nav_bar_section} nav a.tnb-nav-btn"

    def is_component_displayed(self):
        expect(self.page.locator(self._top_nav_bar_section)).to_be_visible()

    def get_nav_header_elements(self):
        elements = self.page.query_selector_all(self._top_nav_header_elements)
        return [element.inner_text().strip() for element in elements]
