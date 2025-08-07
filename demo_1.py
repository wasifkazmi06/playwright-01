from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    #page.wait_for_load_state("networkidle", timeout=60_000)
    login_issue = True
    while login_issue:
        if page.get_by_role("button", name="Log In").first.is_visible():
            page.get_by_role("button", name="Log In").first.click()

    page.get_by_test_id("signUp.switchToSignUp").click()
    page.get_by_role("button", name="Log in with Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").click()
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").fill("wasifkazmi06@gmail.com")
    page.get_by_test_id("emailAuth").get_by_role("textbox", name="Email").press("Tab")
    page.get_by_role("textbox", name="Password").press("CapsLock")
    page.get_by_role("textbox", name="Password").fill("Test@#1234")
    page.get_by_test_id("submit").get_by_test_id("buttonElement").click()
    print("Yay!")
    page.get_by_test_id("handle-button").click()
    page.get_by_role("menuitem", name="My Orders").click()
    page.wait_for_load_state("networkidle", timeout=60_000)
    profile_name_element = page.locator('[data-hook="ProfileCard-memberName"]')
    profile_name_text = profile_name_element.inner_text()
    print(profile_name_text)
    expect(profile_name_element).to_be_visible()
    assert profile_name_text == "wasifkazmi06"
    page.screenshot(path="demo_1.jpg")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
