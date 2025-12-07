from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page: Page = page

    def click(self, locator):
        locator.click()

    def type(self, locator, text):
        locator.fill(text)

    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")
