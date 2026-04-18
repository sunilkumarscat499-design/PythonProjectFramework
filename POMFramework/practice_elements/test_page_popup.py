import pytest
from playwright.sync_api import Playwright, expect



@pytest.mark.skip
def test_check_box(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    child = list()
    page.goto("https://testautomationpractice.blogspot.com/")
    page.on("popup", lambda popup:popup.wait_for_load_state())
    page.locator("#PopUp").hover(force = True)
    page.locator("#PopUp").click()
    page.wait_for_timeout(5000)
    popup_list = context.pages

    text1 = context.pages[1].get_by_text("Register now!")
    text1.click()
    page.wait_for_timeout(5000)



