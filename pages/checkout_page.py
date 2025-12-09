from utils.logger import logger
from .base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)   #https://automationexercise.com/checkout
        self.cart_button= page.locator("(//a[@href = '/view_cart'])[1]")
        self.cart_product_list = page.locator("//tr[contains(@id, 'product-')]").all()
        self.add_comment_about_your_order = page.locator("//textarea[@class='form-control']")
        self.place_order= page.get_by_role("button", name="Place Order")

    def total_price_of_carts(self):
        total = 0
        for  element in self.cart_product_list:
            value = element.locator("//p[@class='cart_total_price']").inner_text()
            total += int(value.removeprefix("Rs. "))
        logger.info(f"Total price is:Rs {total/2}")
        return total/2

    def add_comment_about_order(self, message=""):
        self.add_comment_about_your_order.fill(message)
        logger.info(f"Added message in comment: {message}")

    def click_place_order(self):
        self.place_order.click()
        logger.info(f"....Placed order....")
