
from playwright.sync_api import expect,Page
import pytest
import json
import csv
import openpyxl
workbook1 = openpyxl.load_workbook("testdata/data.xlsx")
sheet = workbook1.worksheets[0] #or workbook1.active
list_data = [(str(x),str(y),str(z)) for x,y,z in sheet.iter_rows(min_row=2, values_only=True)]
workbook1.close()

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

