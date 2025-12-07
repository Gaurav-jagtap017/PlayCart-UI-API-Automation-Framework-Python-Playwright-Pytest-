from .base_page import BasePage

class HomePage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.login_link = page.get_by_role("link", name="Signup / Login")
        self.products_link = page.get_by_role("link", name="Products")

    def open_login(self):
        self.click(self.login_link)

    def open_products(self):
        self.click(self.products_link)
