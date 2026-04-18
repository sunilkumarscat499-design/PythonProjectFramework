from playwright.sync_api import Page, expect, Playwright


def test_trace(playwright:Playwright):
    ## we can open trace.zip by below command
    ## playwright show-trace trace.zip
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demowebshop.tricentis.com/")
    page.locator(".ico-login").click()
    page.locator("#Email").fill("sunil@123.com")
    page.locator("#Password").fill("123456")
    page.wait_for_timeout(5000)
    assert True == False
    context.close()
    browser.close(  )