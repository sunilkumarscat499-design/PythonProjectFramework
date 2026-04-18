import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip
def test_mouse(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("button[ondblclick='myFunction1()']").dblclick()
    page.wait_for_timeout(5000)
    page.locator(".draggable").hover(force=True)
    source = page.locator("#draggable")
    target = page.locator("#droppable")
    source.drag_to(target)
    page.wait_for_timeout(10000)