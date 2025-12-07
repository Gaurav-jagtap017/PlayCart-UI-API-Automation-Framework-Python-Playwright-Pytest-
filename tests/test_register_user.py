from pages.register_page import RegisterPage
from playwright.sync_api import expect
import time
from utils.api_helper import APIclient
from utils.logger import logger

def test_register_valid_user(page):  # use snake_case
    register_page = RegisterPage(page)
    
    register_page.goto_register_page() 

    # match actual text case or use visibility/assertions that don't depend on exact casing
    expect(register_page.account_info).to_be_visible()
    expect(register_page.address_info).to_be_visible()
    register_page.enter_details_and_create_user()

    expect(page.get_by_text("Account Created!")).to_be_visible()
    APIclient.delete_user_api(register_page.email_text, "RandomPass@123")
