from logging import exception

from pages.register_page import RegisterPage
from playwright.sync_api import expect
import time
from utils.api_helper import APIclient
from utils.logger import logger

def test_register_valid_user(page):  # use snake_case
    register_page = RegisterPage(page)

    register_page.goto_register_page()
    logger.info(f"Entered email is: {register_page.email_text} and entered random pass is: {register_page.password_text}.")
    # match actual text case or use visibility/assertions that don't depend on exact casing
    expect(register_page.account_info).to_be_visible()
    expect(register_page.address_info).to_be_visible()
    register_page.enter_details_and_create_user()

    expect(page.get_by_text("Account Created!")).to_be_visible()
    logger.info("Successfully navigated to registration page.")
    register_page.continue_button.click()
    expect(page).to_have_url("https://automationexercise.com/")
    logger.info(f"Successfully navigated to back to main page. Url: {page.url}")
    #Cleanup..
    try :
        APIclient.delete_user_api(register_page.email_text, register_page.password)
    except exception as e:
        logger.info("Retrying to delete user")
        APIclient.delete_user_api(register_page.email_text, register_page.password)
