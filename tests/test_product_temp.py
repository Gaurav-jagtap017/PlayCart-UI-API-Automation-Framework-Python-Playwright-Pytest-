from pages.home_page import HomePage
import time

def test_product_page(setup):
    page = setup
    page.goto("https://automationexercise.com/products")

    # make the first product's overlay visible, then click the Add to cart link
    product = page.locator(".product-image-wrapper")
    #product.scroll_into_view_if_needed()
    product.locator(has_text="Sleeveless Dress")
    product.hover()
    page.locator("a:has-text('Add to cart')").first.click()

    # wait for confirmation and view cart
    page.get_by_text("Added!").wait_for(timeout=5000)
    page.get_by_role("link", name="View Cart").click()
    time.sleep(4)