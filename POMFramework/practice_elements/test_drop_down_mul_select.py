import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
def test_drop_down(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    animals = page.locator("#animals")
    animals.hover(force= True)
    animals.select_option(["Cat","Deer", "Dog"]) # select multiple options
    animal_all = page.locator("#animals>option").all_inner_texts() # get all the select options
    animal_list = [text.strip() for text in animal_all] # store them in list
    print(animal_list)
    copy_list = sorted(animal_list)
    # copy_list = sorted(animal_list , reverse = True) this will reverse sort
    print("copied list is", copy_list)
    assert copy_list == animal_list
    page.wait_for_timeout(5000)


