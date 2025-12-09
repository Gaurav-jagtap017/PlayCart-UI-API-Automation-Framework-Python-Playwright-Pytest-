from playwright.sync_api import sync_playwright
import pytest
import os
from datetime import datetime
import time
import requests
import uuid
from pages.login_page import LoginPage
from playwright.sync_api import expect
from utils.logger import logger

# register placeholder for pytest-html plugin
pytest_html = None

def pytest_configure(config):
    # get the pytest-html plugin instance (if installed)
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://automationexercise.com/login")
        yield page
        browser.close()

@pytest.fixture(autouse=True)
def my_autouse_decorator_fixture(request):
    # Get the name of the test function
    # request.node.originalname is safer for parameterized tests
    function_name = request.node.originalname if hasattr(request.node, 'originalname') else request.node.name

    start_time = time.time()
    print(f"\n--- Decorator Start: Executing '{function_name}' ---")

    yield  # This is where the test function runs

    end_time = time.time()
    duration = end_time - start_time
    print(f"--- Decorator End: Finished '{function_name}' (Duration: {duration:.4f}s) ---")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("page")

        if driver:
            try:
                screenshot_dir = "screenshots"
                os.makedirs(screenshot_dir, exist_ok=True)

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(
                    screenshot_dir, f"{item.name}_{timestamp}.png"
                )

                # Playwright page.screenshot(...) — ensure driver is a Playwright Page
                driver.screenshot(path=screenshot_path)

                # attach to pytest-html safely
                if pytest_html:
                    extra = getattr(report, "extra", [])
                    extra.append(pytest_html.extras.image(screenshot_path))
                    report.extra = extra
            except Exception:
                # don't break pytest reporting if screenshot fails
                pass

@pytest.fixture(scope="session")
def create_user():
    logger.info(f"Started:  create_user")
    unique = uuid.uuid4().hex[:6]
    payload = {
        "email": f"gaurav017{unique}@autotest.com",
        "password": "Autotestg@017"
    }
    new_user_details = {"name": "abcd", "email": f"gaurav017{unique}@autotest.com", "password": "Autotestg@017", "title": "Mr",
                        "birth_date": 30, "birth_month": 3, "birth_year": 2000, "firstname": "abcd",
                        "lastname": "efg017", "company": "xyz", "address1": "lala", "address2": "ok",
                        "country": "india", "zipcode": 414050, "state": "Maharastra", "city": "Pune",
                        "mobile_number": 5431001234}
    user_details= {"user_email_password": payload,
                   "new_user_details": new_user_details}

    response = requests.post("https://automationexercise.com/api/createAccount", data=new_user_details)
    assert response.status_code == 200 or 201
    logger.info(f"successfully created new user: {payload['email']}")
    yield user_details
#    new_response = requests.delete("https://automationexercise.com/api/deleteAccount", data= payload)
#    assert response.status_code == 200 or 404
