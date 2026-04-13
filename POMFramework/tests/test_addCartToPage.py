import pytest
from playwright.sync_api import Page, expect

from POMFramework.src import pages
from POMFramework.src.pages.LoginPage import LoginPage
from POMFramework.src.pages.HomePage import HomePage
from POMFramework.src.pages.cart_page import CartPage


@pytest.mark.parametrize("username, password,\
product_name",[("sunilkumarscat499@gmail.com", \
                "Arjith@123", "Samsung Galaxy S20")])
def test_user_add_Product_toCart(page: Page,username, password, product_name):
    page.goto("https://www.demoblaze.com/index.html")

    #Login page
    login = LoginPage(page)
    login.click_login_link()
    login.enter_username(username)
    login.enter_password(password)
    login.click_on_login_button()

    #Home page
    home_page = HomePage(page)
    home_page.add_product_to_cart(product_name)
    home_page.goto_cart()

    #Cartpage

    # cart_page = CartPage(page)
    # product_in_cart = cart_page.check_product_in_cart(product_name)

    #assert
    # expect(product_in_cart).to_be_visible()