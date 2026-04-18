import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_drop_down(page:Page):
    page.goto("https://bstackdemo.com/")
    page.locator(".sort").hover(force= True)
    page.locator(".sort>select").select_option(label="Lowest to highest")
    page.wait_for_timeout(5000)
    mobile_list = page.locator(".shelf-item__title")
    expect(mobile_list).to_have_count(25)
    mobile_list = [str(x).strip() for x in mobile_list.all_inner_texts()]
    print(mobile_list)

    price_list = page.locator(".shelf-item__price>div>b")
    price_list_num = page.locator(".shelf-item__price>div>b").all_inner_texts()
    print("list length", len(price_list_num))
    expect(price_list).to_have_count(50)
    odd_list = []
    for x in range(0,len(price_list_num),2):
        odd_list.append(price_list_num[x])

    odd_list1 = sorted(odd_list)
    print(f"ordered list is {odd_list}")

    for x,y in zip(mobile_list,odd_list):
        print(f"phone name is {x} and price is {y}")










