from .base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.first_product_add_cart = page.get_by_role("button", name="Add to cart").first
        self.cart_icon = page.get_by_role("link", name="Cart")

    def add_first_product_to_cart(self):
        self.first_product_add_cart.click()

    def open_cart(self):
        self.cart_icon.click()
