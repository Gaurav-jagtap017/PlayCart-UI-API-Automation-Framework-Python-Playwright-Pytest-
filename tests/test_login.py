from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.api_helper import APIclient
from utils.logger import logger

def test_valid_login(page, create_user):
    login_page = LoginPage(page)
    expect(page.get_by_text("Login to your account")).to_be_visible()
    users = create_user["user_email_password"]
    email = users["email"]
    password = users["password"]
    try:
        login_page.login(email, password)
        expect(page.get_by_text("Logged in as")).to_be_visible()

    except AssertionError as e:
        logger.error(f"Login assertion failed: {e}")
        # Re-raise the exception so Pytest marks the test as FAILED
        raise
    finally:
        logger.info(f"Ensuring user {email} is deleted in finally block.")
        APIclient.delete_user_api(email, password)

def test_invalid_login(page):
    login_page = LoginPage(page)
    try:
        login_page.login("random@testmail.com", "random@1223password")
        expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()

    except AssertionError as e:
        logger.error(f"Login assertion failed: {e}")
        # Re-raise the exception so Pytest marks the test as FAILED
        raise







