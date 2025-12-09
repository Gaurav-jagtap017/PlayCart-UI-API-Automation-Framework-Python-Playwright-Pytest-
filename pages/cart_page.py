from playwright.sync_api import expect

from utils.logger import logger
from .base_page import BasePage

class CartPage:
    def __init__(self, page):  #https://automationexercise.com/view_cart
        self.page = page
        self.cart_button= page.locator("(//a[@href = '/view_cart'])[1]")
        self.cart_product_list = page.locator("//tr[contains(@id, 'product-')]").all()
        self.proceed_to_checkout_button = page.get_by_role("button", name="Proceed To Checkout")
        self.list_of_items_in_table= page.locator("//tbody//tr").all()
        self.no_of_columns= page.locator("//thead//tr//td").all()
        self.item_checklist= ["cart_product", "cart_description","cart_price", "cart_quantity", "cart_total", "cart_delete"]

    def check_table_details(self):
        all_details=["cart_description","cart_price", "cart_quantity", "cart_total"] #parameters added for understanding the values.
        logger.info(f"list_of_items_in_table: {len(self.list_of_items_in_table)}")
        for index, item in enumerate(self.list_of_items_in_table):
            # 1. Extract the text values into temporary variables
            description_text = item.locator(f"td.{self.item_checklist[1]}").inner_text()
            price_text = item.locator(f"td.{self.item_checklist[2]}").inner_text()
            quantity_text = item.locator(f"td.{self.item_checklist[3]}").inner_text()
            total_text = item.locator(f"td.{self.item_checklist[4]}").inner_text()

            # 2. Log the variables (logger.info is a one-way operation)
            logger.info(f"cart_description: {description_text}")
            logger.info(f"cart_price: {price_text}")
            logger.info(f"cart_quantity: {quantity_text}")
            logger.info(f"cart_total: {total_text}")
            logger.info("\n")
            # 3. Extend the list with the actual STRING values
            all_details.extend([
                description_text,
                price_text,
                quantity_text,
                total_text
            ])
        return all_details[:]

    def check_added_products(self):
        return self.cart_product_list

    def open_checkout_page(self):
        self.proceed_to_checkout_button.click()
        logger.info("proceed_to_checkout button clicked")

    def go_to_cart(self):
        # Playwright auto-waits for this locator to be clickable before acting
        self.cart_button.click()
