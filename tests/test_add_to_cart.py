from pages.home_page import HomePage
from pages.product_page import ProductPage

def test_add_product_to_cart(setup):
    page = setup
    home = HomePage(page)
    home.open_products()

    product = ProductPage(page)
    #product.add_first_product_to_cart()

    page.get_by_role("link", name="Continue Shopping").click()
    product.open_cart()

    assert page.get_by_text("Product").first.is_visible()
