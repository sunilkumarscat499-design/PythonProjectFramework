import pytest
from playwright.sync_api import Page,expect

'''
1.Allure report is thrird party
2.plugin should be downloaded allure-pytest and allure command line
3.configure allure in pytest.ini
4.attach screenshots on test failures, conftest.py
5.Create and run your tets
6.generate and view the allure report
-- for generating report runtime((allure server generate reports/allure-results))
--permanent generation(allure generate reports/allure-results -o reports/allure-report --clean)
'''

list_items = ["laptop", "gift card", "smartphone", "monitor"]

@pytest.mark.parametrize("item",list_items)
def test_add_items_allure1(page:Page, item):
    page.goto("https://demowebshop.tricentis.com/")
    input_box = page.locator("input[type='text']").nth(0)
    input_box.fill(item)
    search_button = page.locator("input[type='submit']").nth(0)
    search_button.click()
    result_pr = page.locator("h2>li").nth(0)## here actual is "h2>a" cahnged to fail
    expect(result_pr).to_contain_text(item,ignore_case=True)


def test_add_items_allure2(page:Page):

    for x in range(1,10,-1):
        print(x)

@pytest.mark.skip(reason="skipped")
def test_add_items_allure3(page: Page):

    for x in range(1, 10, -1):
        print(x)

@pytest.mark.sanity
def test_add_items_allure4(page: Page):

    for x in range(1, 10, -1):
        print(x)

@pytest.mark.regression
def test_add_items_allure5(page: Page):

    for x in range(1, 10, -1):
        print(x)
