from playwright.sync_api import expect

from website.page.base_page import BasePage

class HomePage(BasePage):

    __LEARN_TO_CODE_CONTENT = ".w3-center.herosection"

    def is_current_page_opened(self):
        expect(self.page.locator(self.__LEARN_TO_CODE_CONTENT)).to_be_visible()