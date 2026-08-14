import allure
from playwright.sync_api import sync_playwright, expect
import pytest

# @pytest.fixture()
# def page():
#     with sync_playwright() as p:
#             browser = p.chromium.launch()
#             context = browser.new_context()
#             page = context.new_page()
#             yield
#             page.close()

@pytest.fixture()
def navigateToAmazon(page):
    page.goto("https://www.amazon.in/") 

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        page = item.funcargs.get("page")
        # page.screenshot()
        if page:
            allure.attach(page.screenshot(), 
                          name="failedpage", 
                          attachment_type=allure.attachment_type.PNG)