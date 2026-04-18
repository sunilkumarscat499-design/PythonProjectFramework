
from playwright.sync_api import expect,Page
import pytest
import json
import csv

file = open("testdata/data.csv",newline = "" ,encoding = "utf-8" )
csv_file = csv.DictReader(file) # stores each row to dictionary
list_data = [(data["email"],data["password"], data["validation"]) for data in csv_file]

@pytest.mark.parametrize("username,password,result",list_data)
def test_mul_login(page:Page, username, password, result):
    page.goto("https://demowebshop.tricentis.com/login")
    email = page.locator("#Email")
    pwd = page.locator("#Password")
    email.fill(username)
    pwd.fill(password)
    login = page.locator("input[value='Log in']")
    login.click()
    account_login_after = page.locator(".account").nth(0)
    error_message = page.locator(".validation-summary-errors>span")

    if result == "valid":
        expect(account_login_after).to_contain_text(username, ignore_case = True)



    if result == "invalid":
        expect(error_message).to_contain_text("Login was unsuccessful. Please correct the errors and try again.")

