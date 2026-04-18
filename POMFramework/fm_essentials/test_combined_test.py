import pytest
from playwright.sync_api import Page, expect, Playwright

@pytest.mark.skip
def test_rerun_trace_capture1(page:Page):
    ## we can open trace.zip by below command
    ## playwright show-trace trace.zip

    page.goto("https://demowebshop.tricentis.com/")
    page.locator(".ico-login").click()
    page.locator("#Email").fill("sunil@123.com")
    page.locator("#Password").fill("123456")
    page.wait_for_timeout(5000)
    assert True == False

@pytest.mark.skip
def test_rerun_trace_capture2(page:Page):
    ## we can open trace.zip by below command
    ## playwright show-trace trace.zip

    page.goto("https://demowebshop.tricentis.com/")
    expect(page).to_have_title("Demo Web Shop")
