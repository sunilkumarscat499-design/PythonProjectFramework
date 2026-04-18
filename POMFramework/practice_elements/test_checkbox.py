import pytest
from playwright.sync_api import Playwright, expect

@pytest.mark.skip
def test_check_box(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")
    sunday_check = page.locator("#sunday")
    expect(sunday_check).to_be_visible()
    expect(sunday_check).to_be_enabled()
    expect(sunday_check).not_to_be_checked()
    sunday_check.hover(force = True)
    sunday_check.check()
    expect(sunday_check).to_be_checked()
    page.wait_for_timeout(5000)
    list_days = ["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]

    checkboxes = [page.get_by_label(x) for x in list_days]

    ## print number of checkboxes
    print(f"number of checkboxes are {len(checkboxes)}")

    ## select all the checkboxes
    for day in list_days:
        box = page.get_by_label(day + "")
        if box.is_checked():
            box.uncheck()
        box.check()
    page.wait_for_timeout(5000)


