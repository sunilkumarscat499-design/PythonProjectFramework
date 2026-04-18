from playwright.sync_api import Page,expect
from POMFramework.src.pages.login_link import Login
from POMFramework.src.pages.login_landing_page import LoginLandingPage
from POMFramework.src.pages.product_store_page import ProductStorePage

def test_add_product_to_cart(page:Page):
    page.goto("https://demoblaze.com/index.html")
    login_link_element = Login(page)
    login = LoginLandingPage(page)
    product_cart = ProductStorePage(page)

    login_link_element.click_on_login_link()
    login.perform_login("sunilkumarscat499@gmail.com","Arjith@123")
    product_cart.go_to_cart()
    expect(page.locator("td").nth(1)).to_contain_text("Samsung galaxy s6")



