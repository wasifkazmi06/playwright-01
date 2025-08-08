import os

import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright, Page
from utilities import configReader


@pytest.fixture(params=["chrome"], scope="function")
def browser(request):
    browser_type = request.param

    with sync_playwright() as p:
        if browser_type == "chrome":
            browser = p.chromium.launch(headless=False)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=False)
        else:
            raise ValueError(f"Unsupported browser : {browser_type}")
        yield browser
        browser.close()


@pytest.fixture(autouse=True)
def setup_function(page):
    page.goto(configReader.readConfig("basic info", "testsiteurl"))


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(record_video_dir="report/videos/")
    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    global page
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page
    page.wait_for_timeout(2000)
    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")
    page.close()
    context.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        # Assuming 'page' fixture is available and provides a Playwright Page object
        # You might need to adjust how you get the 'page' object based on your test setup.
        try:
            page: Page = item.funcargs['page'] # Access the page object from the fixture
            screenshot_dir = "report/failed_screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_failure.png")
            page.screenshot(path=screenshot_path)
            print(f"\nScreenshot saved for failed test: {screenshot_path}")
        except Exception as e:
            print(f"\nCould not take screenshot on failure: {e}")
