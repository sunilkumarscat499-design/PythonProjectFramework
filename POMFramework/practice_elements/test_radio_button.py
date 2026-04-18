import pytest
from playwright.sync_api import Playwright, expect

@pytest.mark.skip
def test_radio_button(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    radio_button = page.locator("#male")
    radio_button.hover(force = True)
    expect(radio_button).to_be_visible()
    expect(radio_button).to_be_enabled()
    expect(radio_button).not_to_be_checked()
    radio_button.check()
    expect(radio_button).to_be_checked()

    page.wait_for_timeout(5000)



