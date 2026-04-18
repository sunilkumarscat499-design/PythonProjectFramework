import pytest
from playwright.sync_api import Page,expect

list_items = ["laptop", "gift card", "smartphone", "monitor"]

@pytest.mark.parametrize("item",list_items)
def test_add_items(page:Page, item):
    page.goto("https://demowebshop.tricentis.com/")
    input_box = page.locator("input[type='text']").nth(0)
    input_box.fill(item)
    search_button = page.locator("input[type='submit']").nth(0)
    search_button.click()
    result_pr = page.locator("h2>a").nth(0)
    expect(result_pr).to_contain_text(item,ignore_case=True)
