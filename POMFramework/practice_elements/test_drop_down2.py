import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_drop_down(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    colors = page.locator("#colors")
    colors.hover(force= True)
    colors.select_option(index = 2)
    page.wait_for_timeout(5000)

    text_colors = page.locator("#colors>option").all_inner_texts()
    print(text_colors)


