from pages.home_page import HomePage
from pages.login_page import LoginPage

def test_valid_login(setup, load_user):
    page = setup
    home = HomePage(page)
    home.open_login()

    login = LoginPage(page)
    login.login(load_user["email"], load_user["password"])

    assert page.get_by_text("Logged in as").is_visible()
