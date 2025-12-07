from playwright.sync_api import sync_playwright
import pytest
import os
from datetime import datetime

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

