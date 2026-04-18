import pytest
from playwright.sync_api import Playwright, expect

@pytest.mark.skip
def test_input_box(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    #here lets call the etxt box using css
    text_box = page.locator("#name")
    expect(text_box).to_be_visible() #element visible
    expect(text_box).to_be_enabled() #element enabled

    ##if you want to validate the other attributes or properities for the element
    expect(text_box).to_have_attribute("maxlength","15")
    max_length = text_box.get_attribute("maxlength")
    assert max_length == "15"

    text_box.fill("filled text") # added value in textbox
    input_added = text_box.input_value() # get value you have given above
    print(f"input added into textbox is {input_added}")

    page.wait_for_timeout(5000)



