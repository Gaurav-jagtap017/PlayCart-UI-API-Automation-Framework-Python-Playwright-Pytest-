import pytest
from playwright.sync_api import Page, expect
from pages.cart_page import CartPage
from utils.api_helper import APIclient
from utils.logger import logger
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

def test_add_product_to_cart(page, create_user):
    login_page = LoginPage(page)
    expect(page.get_by_text("Login to your account")).to_be_visible()
    users = create_user["user_email_password"]
    email = users["email"]
    password = users["password"]
    login_page.login(email, password)
    try:
        for i in range(1,6,2):   #because hidden add to card buttons are there at even index position so taking only odd indexes.
            value = f"(//a[@class='btn btn-default add-to-cart'])[{i}]"
            page.hover(value)
            page.wait_for_timeout(500)
            page.locator(value).click()
            page.get_by_role("button", name="Continue Shopping").click()
        cart_page = CartPage(page)
        cart_page.go_to_cart()
        expect(page.locator("//tbody//tr").first).to_be_visible()
        cart_page = CartPage(page)
        all_table_details = cart_page.check_table_details()
        logger.info(f"all_table_details: {all_table_details}")
        checkoutPage = CheckoutPage(page)
        total = checkoutPage.total_price_of_carts()
        logger.info(f"total price is: {total}")

    finally:
        logger.info(f"Ensuring user {email} is deleted in finally block.")
        APIclient.delete_user_api(email, password)
