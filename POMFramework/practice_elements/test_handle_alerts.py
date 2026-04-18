import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_drop_down(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # page.on("dialog",lambda dialog:dialog.accept())
    # page.locator("#alertBtn").hover(force= True)
    # page.locator("#alertBtn").click()
    # page.wait_for_timeout(2000)

    #
    # page.on("dialog", lambda dialog: dialog.dismiss())
    # page.locator("#confirmBtn").hover(force= True)
    # page.locator("#confirmBtn").click()
    # page.wait_for_timeout(2000)


    page.on("dialog", lambda dialog: dialog.accept("Sunil vadde"))
    page.locator("#promptBtn").hover(force= True)
    page.locator("#promptBtn").click()
    page.wait_for_timeout(5000)