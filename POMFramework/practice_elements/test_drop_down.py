import pytest
from playwright.sync_api import Page, expect
@pytest.mark.skip
def test_drop_down(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    countries = page.locator("#country")
    countries.hover(force= True)
    countries.select_option(label="Canada")
    all_countries =  page.locator("#country>option")
    expect(all_countries).to_have_count(10)
    # get all the country names in drop down

    country_names = [text.strip() for text in all_countries.all_inner_texts()]
    print(country_names)

    page.wait_for_timeout(5000)

