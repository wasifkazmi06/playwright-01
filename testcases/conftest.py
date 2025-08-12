import os
import allure
import pandas
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


@pytest.fixture(scope="function")
def page(browser, request):
    context = browser.new_context(record_video_dir="report/videos/")
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    global page
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    section, url = request.param
    page.goto(configReader.readConfig(section, url))
    yield page
    page.wait_for_timeout(2000)
    context.tracing.stop(path="report/trace.zip")
    page.close()
    context.close()


@pytest.fixture(scope="session")
def read_csv_data_panda(file):
    file_path = configReader.readConfig("data_files", file)
    data = []
    df = pandas.read_csv(file_path)
    for row in df:
        data.append(row)
    print(data)
    return data


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            page: Page = item.funcargs['page']
            screenshot_dir = "report/failed_screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_failure.png")
            page.screenshot(path=screenshot_path)
            allure.attach(page.screenshot(path=screenshot_path), name="failure_screenshot",
                          attachment_type=AttachmentType.PNG)
            print(f"\nScreenshot saved for failed test: {screenshot_path}")
        except Exception as e:
            print(f"\nCould not take screenshot on failure: {e}")
